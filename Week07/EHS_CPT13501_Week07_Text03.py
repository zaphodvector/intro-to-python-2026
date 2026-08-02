"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week07_Text03
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-03-04
    Purpose:	The purpose of this program is to redact any word from a paragraph that isn't in a 
                predefined list.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-03-04	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
paragraph = (
    "For decades, unidentified flying objects have captured the imagination of scientists, "
    "governments, and ordinary citizens alike. Numerous credible witnesses, including military "
    "pilots and radar operators, have reported encounters with craft exhibiting extraordinary "
    "flight characteristics far beyond known human technology. Secret documents declassified "
    "by intelligence agencies reveal that investigations into these phenomena have been conducted "
    "at the highest levels of government since the 1940s. Spectacular incidents like the Roswell "
    "crash of 1947 and the Belgian wave of 1989 remain unexplained despite exhaustive scrutiny. "
    "Advanced propulsion systems, instantaneous acceleration, and silent hovering suggest either "
    "classified terrestrial programs or something altogether different visiting our skies."
)

no_redact = [
    "a", "an", "the", "about", "above", "across", "after", "against", "along", "among",
    "around", "as", "at", "before", "behind", "below", "beneath", "beside", "between",
    "beyond", "by", "despite", "down", "during", "except", "for", "from", "in", "inside",
    "into", "like", "near", "of", "off", "on", "onto", "opposite", "out", "outside", "over",
    "past", "since", "through", "throughout", "to", "under", "underneath", "until", "up",
    "upon", "with", "within", "without", "and", "but", "or", "nor", "for", "so", "yet",
    "either", "neither", "whether", "although", "because", "since", "while", "as", "unless",
    "if", "until", "before", "after", "than", "as if", "as though", "even though", "in case",
    "lest", "so that", "provided that", "in order that", "though", "if only", "he", "she",
    "it", "they", "we", "you", "I", "me", "him", "her", "them", "us", "my", "mine", "his",
    "her", "hers", "its", "our", "ours", "their", "theirs", "your", "yours", "whose", "this",
    "that", "these", "those", "who", "whom", "which", "what", "whoever", "whomever",
    "whatever", "whichever", "each", "any", "someone", "anyone", "everyone", "no one",
    "somebody", "anybody", "everybody", "nobody", "none", "both", "few", "several", "many",
    "one", "all", "some", "more", "most", "another", "either", "neither", "oh", "wow",
    "hey", "oops", "ah", "uh", "um"
]

def print_wrapped(text, width=80):
    words = text.split()
    line = ""
    for word in words:
        if len(line) + len(word) + (1 if line else 0) <= width:
            line = line + (" " if line else "") + word
        else:
            print(line)
            line = word
    if line:
        print(line)

def redact(text, no_redact):
    words = text.split()
    result = []
    for word in words:
        # Strip punctuation for comparison only
        clean = word.strip(".,!?;:'\"").lower()
        if clean in no_redact:
            result.append(word)
        else:
            result.append("----")
    return " ".join(result)

print("--- ORIGINAL PARAGRAPH ---\n")
print_wrapped(paragraph)

print("\n--- REDACTED PARAGRAPH ---\n")
print_wrapped(redact(paragraph, no_redact))


#I had a busy week, and i do not have the time before the deadline to make comments on this program.