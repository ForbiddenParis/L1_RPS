# functions go here
# check that users have entered a valid option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    """Checks user response is a valid answer in the list"""
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response if the same as
            # the first letter of an item in this list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something that is valid
        print(error)
        print()


def instructions():
    """Print instructions"""
    print('''
**** Instructions ****

To begin, choose the number of rounds (or press <enter> for 
infinite mode).

Then play against the computer. You need to choose R (rock),
P (paper) or S (scissors).

The rules are as follows:
o   Paper Beats rock
o   Rock beats scissors
o   Scissors beats paper

Press <xxx> to end the game anytime

Good Luck!
    ''')


# Main routine
print()
print("🪨📃✂️ Rock / Paper / Scissors Game ✂️📃🪨")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print("Program continues")
