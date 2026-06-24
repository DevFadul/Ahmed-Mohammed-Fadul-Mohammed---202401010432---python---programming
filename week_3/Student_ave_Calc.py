choice = "y"

# Loop continues while the user chooses "y"
while choice == "y":

    # Input three quiz marks from the user
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate the average mark
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Determine if the student passes or fails
    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    # Ask whether to continue with another student
    choice = input("Continue? Select Y/N: ").lower()

print("Program Ended")