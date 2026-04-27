"""
Tone Generator - Proof of Concept
Zelle graphics UI + sounddevice/numpy audio engine

Controls:
  OCT-/OCT+     : octave jump
  NOTE-/NOTE+   : semitone step
  FINE--/FINE-  : -10/-1 cent
  FINE+/FINE++  : +1/+10 cent
  Waveform row  : sine / square / saw / triangle
  STOP/PLAY     : toggle audio
"""

import threading
import numpy as np
import sounddevice as sd
from graphics import GraphWin, Rectangle, Text, Point, color_rgb

# ── Constants ────────────────────────────────────────────────────────────────
SAMPLE_RATE = 44100
CHUNK       = 2048          # frames per audio callback
NOTE_NAMES  = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
WAVEFORMS   = ["sine", "square", "saw", "triangle"]

# A4 = 440 Hz, MIDI note 69
A4_MIDI = 69
A4_HZ   = 440.0

# ── Audio state (shared between UI thread and audio callback) ─────────────
state = {
    "midi":     69,       # semitone index (MIDI note number)
    "cents":    0.0,      # fine tune offset in cents
    "waveform": "sine",
    "playing":  True,
    "phase":    0.0,      # continuous phase accumulator
}
state_lock = threading.Lock()

# ── Frequency helpers ─────────────────────────────────────────────────────

def midi_to_hz(midi, cents=0.0):
    return A4_HZ * 2 ** ((midi - A4_MIDI + cents / 100.0) / 12.0)

def midi_to_name(midi):
    note  = NOTE_NAMES[midi % 12]
    octave = (midi // 12) - 1
    return f"{note}{octave}"

# ── Audio callback ────────────────────────────────────────────────────────

def audio_callback(outdata, frames, time_info, status):
    with state_lock:
        playing  = state["playing"]
        midi     = state["midi"]
        cents    = state["cents"]
        waveform = state["waveform"]
        phase    = state["phase"]

    if not playing:
        outdata[:] = 0
        return

    freq  = midi_to_hz(midi, cents)
    omega = 2.0 * np.pi * freq / SAMPLE_RATE
    t     = phase + omega * np.arange(frames)

    if waveform == "sine":
        wave = np.sin(t)
    elif waveform == "square":
        wave = np.sign(np.sin(t))
    elif waveform == "saw":
        wave = 2.0 * ((t / (2 * np.pi)) % 1.0) - 1.0
    else:  # triangle
        p    = (t / (2 * np.pi)) % 1.0
        wave = 4.0 * np.abs(p - 0.5) - 1.0

    wave = (wave * 0.4).astype(np.float32)
    outdata[:, 0] = wave

    new_phase = (phase + omega * frames) % (2 * np.pi)
    with state_lock:
        state["phase"] = new_phase

# ── Colour palette ────────────────────────────────────────────────────────
BG          = color_rgb(20,  20,  30)
PANEL_BG    = color_rgb(35,  35,  50)
BTN_IDLE    = color_rgb(55,  55,  80)
BTN_HOVER   = color_rgb(80,  80, 120)   # used as "active waveform" tint
BTN_TEXT    = color_rgb(220, 220, 240)
ACCENT      = color_rgb(100, 180, 255)
DISPLAY_BG  = color_rgb(10,  10,  20)
DISPLAY_TXT = color_rgb(100, 255, 160)

# ── Button helper ─────────────────────────────────────────────────────────

class Button:
    """Clickable rectangle with a centered text label drawn in a GraphWin."""

    def __init__(self, win, x1, y1, x2, y2, label, bg=None):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        bg = bg or BTN_IDLE
        self.rect = Rectangle(Point(x1, y1), Point(x2, y2))
        self.rect.setFill(bg)
        self.rect.setOutline(ACCENT)
        self.rect.setWidth(1)
        self.rect.draw(win)
        cx, cy = (x1+x2)/2, (y1+y2)/2
        self.label = Text(Point(cx, cy), label)
        self.label.setTextColor(BTN_TEXT)
        self.label.setSize(10)
        self.label.draw(win)

    def clicked(self, pt):
        return (self.x1 < pt.getX() < self.x2 and
                self.y1 < pt.getY() < self.y2)

    def set_bg(self, col):
        self.rect.setFill(col)

# ── Display panel ─────────────────────────────────────────────────────────

class Display:
    def __init__(self, win, x1, y1, x2, y2):
        bg = Rectangle(Point(x1, y1), Point(x2, y2))
        bg.setFill(DISPLAY_BG)
        bg.setOutline(ACCENT)
        bg.setWidth(2)
        bg.draw(win)
        cx = (x1+x2)/2
        self.note_txt = Text(Point(cx, y1+30), "A4")
        self.note_txt.setTextColor(DISPLAY_TXT)
        self.note_txt.setSize(28)
        self.note_txt.setStyle("bold")
        self.note_txt.draw(win)

        self.hz_txt = Text(Point(cx, y1+60), "440.00 Hz")
        self.hz_txt.setTextColor(DISPLAY_TXT)
        self.hz_txt.setSize(14)
        self.hz_txt.draw(win)

        self.cents_txt = Text(Point(cx, y1+80), "±0 cents")
        self.cents_txt.setTextColor(color_rgb(160, 220, 180))
        self.cents_txt.setSize(11)
        self.cents_txt.draw(win)

        self.wave_txt = Text(Point(cx, y1+100), "▶ sine")
        self.wave_txt.setTextColor(ACCENT)
        self.wave_txt.setSize(11)
        self.wave_txt.draw(win)

        self.status_txt = Text(Point(cx, y1+120), "● PLAYING")
        self.status_txt.setTextColor(color_rgb(100,255,100))
        self.status_txt.setSize(10)
        self.status_txt.draw(win)

    def update(self, midi, cents, waveform, playing):
        hz   = midi_to_hz(midi, cents)
        name = midi_to_name(midi)
        self.note_txt.setText(name)
        self.hz_txt.setText(f"{hz:.2f} Hz")
        sign = "+" if cents >= 0 else ""
        self.cents_txt.setText(f"{sign}{cents:.0f} cents")
        self.wave_txt.setText(f"▶ {waveform}")
        if playing:
            self.status_txt.setText("● PLAYING")
            self.status_txt.setTextColor(color_rgb(100,255,100))
        else:
            self.status_txt.setText("■ STOPPED")
            self.status_txt.setTextColor(color_rgb(255,100,100))

# ── Main ──────────────────────────────────────────────────────────────────

def main():
    W, H = 420, 420
    win  = GraphWin("Tone Generator", W, H)
    win.setBackground(BG)

    # Title
    title = Text(Point(W//2, 18), "TONE GENERATOR  //  proof of concept")
    title.setTextColor(ACCENT)
    title.setSize(11)
    title.draw(win)

    # Display panel
    disp = Display(win, 20, 30, 400, 165)

    # ── Frequency controls ------------------------------------------------
    row1_y  = 178   # octave row
    row2_y  = 218   # semitone row
    row3_y  = 258   # fine tune row
    btn_h   = 32
    col_gap = 6

    # Octave row
    Text(Point(50, row1_y+16), "OCT").setTextColor(color_rgb(160,160,200)), \
    None  # just label — drawn inline below
    lbl_oct = Text(Point(50, row1_y+16), "OCT")
    lbl_oct.setTextColor(color_rgb(160,160,200)); lbl_oct.setSize(9); lbl_oct.draw(win)

    btn_oct_dn = Button(win, 70,  row1_y, 175, row1_y+btn_h, "OCT  ▼")
    btn_oct_up = Button(win, 181, row1_y, 286, row1_y+btn_h, "OCT  ▲")

    # Semitone row
    lbl_note = Text(Point(50, row2_y+16), "NOTE")
    lbl_note.setTextColor(color_rgb(160,160,200)); lbl_note.setSize(9); lbl_note.draw(win)

    btn_note_dn = Button(win, 70,  row2_y, 175, row2_y+btn_h, "NOTE  ▼")
    btn_note_up = Button(win, 181, row2_y, 286, row2_y+btn_h, "NOTE  ▲")

    # Fine tune row
    lbl_fine = Text(Point(50, row3_y+16), "FINE")
    lbl_fine.setTextColor(color_rgb(160,160,200)); lbl_fine.setSize(9); lbl_fine.draw(win)

    btn_fine_dn10 = Button(win, 70,  row3_y, 130, row3_y+btn_h, "−10¢")
    btn_fine_dn1  = Button(win, 136, row3_y, 196, row3_y+btn_h, "−1¢")
    btn_fine_up1  = Button(win, 202, row3_y, 262, row3_y+btn_h, "+1¢")
    btn_fine_up10 = Button(win, 268, row3_y, 328, row3_y+btn_h, "+10¢")

    # Reset cents
    btn_reset = Button(win, 334, row3_y, 400, row3_y+btn_h, "RESET")

    # ── Waveform row -------------------------------------------------------
    row4_y  = 305
    wf_btns = {}
    wf_x    = [20, 115, 210, 305]
    for i, wf in enumerate(WAVEFORMS):
        b = Button(win, wf_x[i], row4_y, wf_x[i]+90, row4_y+btn_h, wf)
        wf_btns[wf] = b
    wf_btns["sine"].set_bg(BTN_HOVER)   # default highlight

    # ── Play/Stop ---------------------------------------------------------
    row5_y = 358
    btn_toggle = Button(win, 130, row5_y, 290, row5_y+40, "■  STOP")

    # ── Footer note -------------------------------------------------------
    footer = Text(Point(W//2, 408), "click anywhere outside buttons to refresh display")
    footer.setTextColor(color_rgb(70,70,100)); footer.setSize(8); footer.draw(win)

    # ── Start audio stream ------------------------------------------------
    stream = sd.OutputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        blocksize=CHUNK,
        callback=audio_callback
    )
    stream.start()

    # ── Event loop --------------------------------------------------------
    def refresh():
        with state_lock:
            m, c, wf, pl = state["midi"], state["cents"], state["waveform"], state["playing"]
        disp.update(m, c, wf, pl)
        # waveform button highlights
        for w, b in wf_btns.items():
            b.set_bg(BTN_HOVER if w == wf else BTN_IDLE)
        btn_toggle.label.setText("■  STOP" if pl else "▶  PLAY")

    while True:
        pt = win.checkMouse()
        if win.isClosed():
            break
        if pt is None:
            continue

        changed = True

        if btn_oct_dn.clicked(pt):
            with state_lock: state["midi"] = max(0,  state["midi"] - 12)
        elif btn_oct_up.clicked(pt):
            with state_lock: state["midi"] = min(127, state["midi"] + 12)
        elif btn_note_dn.clicked(pt):
            with state_lock: state["midi"] = max(0,  state["midi"] - 1)
        elif btn_note_up.clicked(pt):
            with state_lock: state["midi"] = min(127, state["midi"] + 1)
        elif btn_fine_dn10.clicked(pt):
            with state_lock: state["cents"] = max(-100, state["cents"] - 10)
        elif btn_fine_dn1.clicked(pt):
            with state_lock: state["cents"] = max(-100, state["cents"] - 1)
        elif btn_fine_up1.clicked(pt):
            with state_lock: state["cents"] = min(100, state["cents"] + 1)
        elif btn_fine_up10.clicked(pt):
            with state_lock: state["cents"] = min(100, state["cents"] + 10)
        elif btn_reset.clicked(pt):
            with state_lock: state["cents"] = 0.0
        elif btn_toggle.clicked(pt):
            with state_lock: state["playing"] = not state["playing"]
        else:
            for wf, b in wf_btns.items():
                if b.clicked(pt):
                    with state_lock: state["waveform"] = wf
                    break
            else:
                changed = False

        if changed:
            refresh()

    stream.stop()
    stream.close()
    win.close()

if __name__ == "__main__":
    main()