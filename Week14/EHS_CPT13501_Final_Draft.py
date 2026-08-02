"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPY13501_Final
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-04-27
    Purpose:	The purpose of this program is to produce a tone that is controllable through a zelle 
                graphics interface. The program will also have a toggle-able inaccuracy switch that the
                user will be able to fix with an array of fine tuning buttons.

                The A.I. of choice for learning the numpy module, the threading module and the 
                sounddevice module was Claude. I also got info on what constants to define for said 
                module. Claude was also given a vague layout for the GUI and gave me back x and y 
                coordinates for the code.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-04-27	Original Version of Code
----------------------------------------------------------------------------------------------------------s
"""
import random
from graphics import *
import sounddevice as sd
import numpy as np
import threading

state_lock = threading.Lock()

SAMPLE_RATE = 44100
CHUNK = 2048
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
A4_MIDI = 69
A4_HZ = 440.0
state = {"note": 69, "tuning": 0, "playing": False, "waveform": "Sine", "drift": 0, "drifting": False, 
         "phase": 0.0}
WAVEFORMS = ["Sine", "Saw", "Square", "Triangle"]

#Variable conversion functions

def midi_to_hz(note, tuning):
    return A4_HZ * 2 ** ((note - A4_MIDI + tuning / 100) / 12)

def midi_to_name(note):
    return NOTE_NAMES[note % 12] + str((note // 12) - 1)

def trigger_drift():
    with state_lock:
        state["drift"] = random.randint(-30, 30)

# Graphics

XWIDTH = 500
XHEIGHT = 420

BACKGROUND = color_rgb(37, 78, 112)
#BTN_OUTLINE = color_rgb(195, 60, 84)
BTN_OUTLINE = color_rgb(51, 153, 129)
BTN_TEXT = color_rgb(55, 113, 142)
BTN_COLOR = color_rgb(142, 227, 239)

win = GraphWin("Tone Generator", XWIDTH, XHEIGHT)
win.setBackground(BACKGROUND)

# Current Settings Window
rect = Rectangle(Point(10, 10), Point(490, 165))
rect.setFill("black")
rect.setOutline(BTN_OUTLINE)
rect.setWidth(5)
rect.draw(win)

# Current note
note_txt = Text(Point(250, 30), midi_to_name(state["note"]))
note_txt.setSize(20)
note_txt.setTextColor(BTN_TEXT)
note_txt.draw(win)

# Target Hertz
thz_txt = Text(Point(250, 60), f"Target {midi_to_hz(state['note'], 0):.2f} Hz")
thz_txt.setSize(20)
thz_txt.setTextColor("green")
thz_txt.draw(win)

# Actual Hertz
ahz_txt = Text(Point(250, 90), f"Actual {midi_to_hz(state['note'], state['tuning'] + state['drift']):.2f} Hz")
ahz_txt.setSize(20)
ahz_txt.setTextColor(color_rgb(140, 43, 61))
ahz_txt.draw(win)

# Waveform
wave_txt = Text(Point(250, 120), state["waveform"])
wave_txt.setSize(20)
wave_txt.setTextColor(BTN_TEXT)
wave_txt.draw(win)

# User Tuning
tune_txt = Text(Point(250, 150), f"{state['tuning']} Cents")
tune_txt.setSize(20)
tune_txt.setTextColor(BTN_TEXT)
tune_txt.draw(win)

def update_display():
    note_txt.setText(midi_to_name(state["note"]))
    ahz_txt.setText(f"Actual {midi_to_hz(state['note'], state['tuning'] + state['drift']):.2f} Hz")
    thz_txt.setText(f"Target {midi_to_hz(state['note'], 0):.2f} Hz")
    wave_txt.setText(state["waveform"])
    tune_txt.setText(f"{state['tuning']} Cents")

class Button:
    def __init__(self, win, x1, y1, x2, y2, label):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.button = Rectangle(Point(x1, y1), Point(x2, y2))
        self.button.setFill(BTN_COLOR)
        self.button.setOutline(BTN_OUTLINE)
        self.button.setWidth(3)
        self.button.draw(win)
        btn_text = Text(Point((x1 + x2)/2, (y1 + y2)/2), label)
        btn_text.setSize(13)
        btn_text.setTextColor(BTN_TEXT)
        btn_text.draw(win)

    def clicked(self, pt):
       return self.x1 < pt.getX() < self.x2 and self.y1 < pt.getY() < self.y2
    
    def set_color(self, color):
        self.button.setFill(color)
    
# Main audio creation function

def audio_callback(outdata, frames, time_info, status):

    with state_lock:
        note = state["note"]
        tuning = state["tuning"]
        drift = state["drift"]
        waveform = state["waveform"]
        playing = state["playing"]
        phase = state["phase"]

    if not playing:
        outdata[:] = 0
        return

    freq = midi_to_hz(note, tuning + drift)

    t = phase + np.arange(frames) * (2 * np.pi * freq / SAMPLE_RATE)

    new_phase = (phase + frames * 2 * np.pi * freq / SAMPLE_RATE) % (2 * np.pi)
    with state_lock:
        state["phase"] = new_phase

    if waveform == "Sine":
        wave = np.sin(t)
    elif waveform == "Square":
        wave = np.sign(np.sin(t))
    elif waveform == "Saw":
        wave = (((t / (2 * np.pi)) % 1.0) *2) -1
        '''(t / 2π) % 1.0      # ramp from 0 to 1, repeating
        * 2                    # stretch to 0 to 2
        - 1                    # shift to -1 to 1'''
    elif waveform == "Triangle":
        wave = ((np.abs(((t / (2 * np.pi)) % 1.0) - 0.5)) * 4) - 1
        '''(t / 2π) % 1.0      # ramp 0 to 1
        subtract 0.5           # center it: -0.5 to 0.5
        abs()                  # fold: 0 to 0.5 to 0
        multiply by 4          # stretch: 0 to 2 to 0
        subtract 1             # shift: -1 to 1 to -1'''
    wave = (wave * 0.4).astype(np.float32)
    outdata[:, 0] = wave
#❚❚ ▶

oct_dn = Button(win, 35, 185, 135, 225, "OCT ▼")
oct_up = Button(win, 365, 185, 465, 225, "OCT ▲")

nte_dn = Button(win, 145, 185, 245, 225, "NOTE ▼")
nte_up = Button(win, 255, 185, 355, 225, "NOTE ▲")

tenc_dn = Button(win, 35, 245, 135, 285, "-10¢")
onec_dn = Button(win, 145, 245, 245, 285, "-1¢")
onec_up = Button(win, 255, 245, 355, 285, "+1¢")
tenc_up = Button(win, 365, 245, 465, 285, "+10¢")

sine_tg = Button(win, 35, 305, 135, 345, "SINE")
saw_tg = Button(win, 145, 305, 245, 345, "SAW")
square_tg = Button(win, 255, 305, 355, 345, "SQUARE")
triangle_tg = Button(win, 365, 305, 465, 345, "TRIANGLE")

tone_tg = Button(win, 35, 365, 245, 395, "Toggle On/Off")
cents_rst = Button(win, 255, 365, 355, 395, "Reset Tuning")
drift_tg = Button(win, 365, 365, 465, 395, "Toggle Drift")

# 

stream = sd.OutputStream(
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    blocksize=CHUNK,
    callback=audio_callback
)
stream.start()

# Button activation checks

while True:
    pt = win.checkMouse()
    if win.isClosed():
        break
    if pt is None:
        continue

    if oct_dn.clicked(pt):
        state["note"] = max(0, state["note"] - 12)
        if state["drifting"]:
            trigger_drift()
    elif oct_up.clicked(pt):
        state["note"] = min(127, state["note"] + 12)
        if state["drifting"]:
            trigger_drift()

    elif nte_dn.clicked(pt):
        state["note"] = max(0, state["note"] - 1)
        if state["drifting"]:
            trigger_drift()
    elif nte_up.clicked(pt):
        state["note"] = min(127, state["note"] + 1)
        if state["drifting"]:
            trigger_drift()

    elif tenc_dn.clicked(pt):
        state["tuning"] = max(-50, state["tuning"] - 10)
    elif onec_dn.clicked(pt):
        state["tuning"] = max(-50, state["tuning"] - 1)
    elif onec_up.clicked(pt):
        state["tuning"] = min(50, state["tuning"] + 1)
    elif tenc_up.clicked(pt):
        state["tuning"] = min(50, state["tuning"] + 10)

    elif sine_tg.clicked(pt):
        state["waveform"] = "Sine"
        sine_tg.set_color(color_rgb(31, 193, 214))
        saw_tg.set_color(BTN_COLOR)
        square_tg.set_color(BTN_COLOR)
        triangle_tg.set_color(BTN_COLOR)
    elif saw_tg.clicked(pt):
        state["waveform"] = "Saw"
        sine_tg.set_color(BTN_COLOR)
        saw_tg.set_color(color_rgb(31, 193, 214))
        square_tg.set_color(BTN_COLOR)
        triangle_tg.set_color(BTN_COLOR)
    elif square_tg.clicked(pt):
        state["waveform"] = "Square"
        sine_tg.set_color(BTN_COLOR)
        saw_tg.set_color(BTN_COLOR)
        square_tg.set_color(color_rgb(31, 193, 214))
        triangle_tg.set_color(BTN_COLOR)
    elif triangle_tg.clicked(pt):
        state["waveform"] = "Triangle"
        sine_tg.set_color(BTN_COLOR)
        saw_tg.set_color(BTN_COLOR)
        square_tg.set_color(BTN_COLOR)
        triangle_tg.set_color(color_rgb(31, 193, 214))

    elif tone_tg.clicked(pt):
        state["playing"] = not state["playing"]
        tone_tg.set_color(color_rgb(31, 193, 214) if state["playing"] else BTN_COLOR)
    elif cents_rst.clicked(pt):
        state["tuning"] = 0
        state["drift"] = 0
    elif drift_tg.clicked(pt):
        state["drifting"] = not state["drifting"]
        drift_tg.set_color(color_rgb(31, 193, 214) if state["drifting"] else BTN_COLOR)
    
    update_display()

stream.stop()
stream.close()