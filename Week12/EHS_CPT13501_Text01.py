"""
----------------------------------------------------------------------------------------------------------
    Name:		EHS_CPT13501_Text01
    Author:		Elijah Schultz
    Language:	Python
    Date:		2026-04-17
    Purpose:	The purpose of this program is to store student information and extrapolate data based 
                on user inputs.

                Text02 took me about 40 seconds so I did this one as well.
----------------------------------------------------------------------------------------------------------
    Change Log
----------------------------------------------------------------------------------------------------------
    Who		Date		Reason
    EHS		2026-04-17	Original Version of Code
----------------------------------------------------------------------------------------------------------
"""
students = []

for i in range(5):
    print(f"\nStudent {i + 1}:")

    while True:
        name = input("Enter student's first name: ").strip()
        try:
            if len(name) < 1 or len(name) > 20:
                raise ValueError
            name = name.title()
            break
        except ValueError:
            print("Name must be between 1 and 20 characters. Try again.")

    while True:
        try:
            age = int(input("Enter student's age: "))
            if age < 1 or age > 110:
                raise ValueError
            break
        except ValueError:
            print("Age must be a whole number between 1 and 110. Try again.")

    students.append((name, age))

# After each iteration getting input from the user, the user's input is

print("\n--- Student Info ---")
for name, age in students:
    print(f"{name}, Age: {age}")

average_age = sum(age for _, age in students) / len(students)
print(f"\nAverage age: {average_age:.2f}")