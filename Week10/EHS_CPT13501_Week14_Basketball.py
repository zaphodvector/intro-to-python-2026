"""
----------------------------------------------------------------------------------------------------------
    Name:       EHS_CPT13501_Week14_Basketball
    Author:     Elijah Schultz
    Language:   Python
    Date:       2026-05-04
    Purpose:    Collects starting lineup information for a basketball team of 5 players
                (name, height in feet and inches) and displays a formatted roster with
                the team's combined and average height. Imports validation functions
                from the Week 10 vacation planner program.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who     Date        Reason
    EHS     2026-05-04  Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from EHS_CPT13501_Week10_VacationPlanner import (
    fncGetUserInput,
    fncValidatePositiveInteger,
    fncValidatePositiveFloat,
)

NUM_PLAYERS = 5
MIN_FEET    = 4
MAX_FEET    = 8
MAX_INCHES  = 11.99


def fncGetPlayerName(playerNum):
    return fncGetUserInput("  Name: ")


def fncGetPlayerFeet(playerNum):
    while True:
        raw = fncGetUserInput("  Height - feet (" + str(MIN_FEET) + " to " + str(MAX_FEET) + "): ")
        if fncValidatePositiveInteger(raw):
            feet = int(raw)
            if MIN_FEET <= feet <= MAX_FEET:
                return feet
        print("  Please enter a whole number between " + str(MIN_FEET) + " and " + str(MAX_FEET) + ".")


def fncGetPlayerInches(playerNum):
    while True:
        raw = fncGetUserInput("  Height - remaining inches (0.0 to 11.99): ")
        if fncValidatePositiveFloat(raw):
            inches = float(raw)
            if 0.0 <= inches <= MAX_INCHES:
                return inches
        print("  Please enter a number between 0.0 and 11.99.")


def fncCollectRoster():
    players = {}
    for i in range(1, NUM_PLAYERS + 1):
        print("\n--- Player " + str(i) + " of " + str(NUM_PLAYERS) + " ---")
        name   = fncGetPlayerName(i)
        feet   = fncGetPlayerFeet(i)
        inches = fncGetPlayerInches(i)
        players[i] = {"name": name, "feet": feet, "inches": inches}
    return players


def fncPrintRoster(players):
    print("\n" + "=" * 52)
    print(" STARTING LINEUP")
    print("=" * 52)
    print(" {:<4} {:<22} {}".format("#", "Name", "Height"))
    print("-" * 52)
    for num, p in players.items():
        height_str = str(p["feet"]) + "' " + format(p["inches"], ".2f") + '"'
        print(" {:<4} {:<22} {}".format(str(num), p["name"], height_str))
    print("=" * 52)


def fncCalculateStats(players):
    total_in = sum(p["feet"] * 12 + p["inches"] for p in players.values())
    avg_in   = total_in / len(players)

    total_ft     = int(total_in // 12)
    total_rem_in = total_in % 12
    avg_ft       = int(avg_in // 12)
    avg_rem_in   = avg_in % 12

    return total_ft, total_rem_in, avg_ft, avg_rem_in


def main():
    print("=" * 52)
    print(" BASKETBALL TEAM ROSTER - STARTING 5")
    print("=" * 52)

    players = fncCollectRoster()
    fncPrintRoster(players)

    total_ft, total_in, avg_ft, avg_in = fncCalculateStats(players)

    print("\n Combined height (head-to-toe): " + str(total_ft) + "' " + format(total_in, ".2f") + '"')
    print(" Average player height:         " + str(avg_ft) + "' " + format(avg_in, ".2f") + '"')
    print()


if __name__ == "__main__":
    main()
