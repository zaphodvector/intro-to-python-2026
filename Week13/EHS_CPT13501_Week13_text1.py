"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Week13_text1
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-04-22
    Purpose:	The purpose of this program is to read contents of a waiver on a txt file, then provide
                a report of expired waivers and the location of the participant's household. This 
                program requires the EHS_CPT13501_Waivers.txt file in the zip file.

                I used AI to generate a list of 100 waivers as well as choosing what type of data to 
                use in the text files(csv or key and value). Also was used for talking myself through the
                writing process.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-04-22	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
def load_waivers(filename):
    waivers = []
    current = {}

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                if current:
                    waivers.append(current)
                    current = {}
            else:
                key, value = line.split(": ", 1)
                current[key] = value

    if current:
        waivers.append(current)

    return waivers

# Creating an empty list for waivers and a temporary dictionary to hold the info of the current waiver 
# being analyzed. After opening the file in read mode it iterates through line by line, splits the string
# at the first colon(to prevent a cascading data storage error), and stores the contents of the line into
# the current dictionary. When it arrives at an empty line the code it appends the collected key and 
# values into the waivers list.  

def analyze_waivers(waivers):
    total        = len(waivers)
    expired      = [w for w in waivers if w["expired"].lower() == "yes"]
    active       = [w for w in waivers if w["expired"].lower() == "no"]
    in_missouri  = [w for w in waivers if w["address"].endswith("MO")]
    out_of_state = [w for w in waivers if not w["address"].endswith("MO")]

    print("=" * 50)
    print("              WAIVER SYSTEM ANALYSIS")
    print("=" * 50)

    print(f"\nTotal waivers in system : {total}")
    print(f"Active waivers          : {len(active)}")
    print(f"Expired waivers         : {len(expired)}")
    print(f"Missouri residents      : {len(in_missouri)}")
    print(f"Out-of-state            : {len(out_of_state)}")

    print("\n" + "-" * 50)
    print(f"EXPIRED WAIVERS ({len(expired)} total)")
    print("-" * 50)
    for w in expired:
        in_state = w["address"].endswith("MO")
        location = "In-state" if in_state else "Out-of-state"
        print(f"  - {w['parent_name']:<25}  [{location}]")

    print("\n" + "=" * 50)

# analyze_waivers takes the completed list of waiver dictionaries and sorts them into four categories
# using list comprehensions.(expired, active, in-state, and out-of-state) Then it prints a summary of
# the totals for each category, followed by a list of expired waivers that flags whether each one 
# belongs to a Missouri resident or not using the endswith() check on the address field.

print("=" * 50)
print("          WELCOME TO THE WAIVER DATABASE")
print("=" * 50)

waivers = load_waivers("EHS_CPT13501_Waivers.txt")
print(f"\n{len(waivers)} waivers loaded successfully.")

while True:
    answer = input("\nWould you like to check for expired waivers? (yes/no): ").strip().lower()

    if answer == "yes":
        analyze_waivers(waivers)
        break
    elif answer == "no":
        print("\nGoodbye!")
        break
    else:
        print("Invalid input. Please type yes or no.")