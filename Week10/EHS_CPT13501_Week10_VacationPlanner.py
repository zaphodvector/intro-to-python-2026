
def fncGetUserInput(prompt):
    userInput = ""
    while userInput == "":
        userInput = input(prompt).strip()
    return userInput


def fncValidatePositiveInteger(s):
    s = s.strip()
    if not s:
        return False
    return s.isdigit()


def fncValidatePositiveFloat(s):
    s = s.strip()
    if not s:
        return False
    if s.count('.') > 1:
        return False
    check = s.replace('.', '', 1)
    if not check:
        return False
    return check.isdigit()


def main():
    # Get vacation spot
    vacationSpot = fncGetUserInput("Where would you like to go for vacation? ")

    # Get number of days (positive non-zero integer)
    daysInput = ""
    while True:
        daysInput = fncGetUserInput("How many days would you like to spend at " + vacationSpot + "? ")
        if fncValidatePositiveInteger(daysInput) and int(daysInput) > 0:
            break
        print("Please enter a valid number of days greater than zero.")
    numDays = int(daysInput)

    # Get budget (positive non-zero float)
    budgetInput = ""
    while True:
        budgetInput = fncGetUserInput("What is your total budget for this vacation? $")
        if fncValidatePositiveFloat(budgetInput) and float(budgetInput) > 0:
            break
        print("Please enter a valid budget amount greater than zero.")
    totalBudget = float(budgetInput)

    # Calculate and display results
    dailyBudget = totalBudget / numDays

    print("\n--- Your Vacation Plan ---")
    print("Destination:          " + vacationSpot)
    print("Days:                 " + str(numDays))
    print("Total Budget:         $" + format(totalBudget, ",.2f"))
    print("Average Daily Budget: $" + format(dailyBudget, ",.2f"))


main()
