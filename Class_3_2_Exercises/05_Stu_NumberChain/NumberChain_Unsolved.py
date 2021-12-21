# Initial variable to track game play
user_play = "y"
loop_target = 0
loop_number = 0
# While we are still playing...
while user_play == "y":

    # Ask the user how many numbers to loop through
    loop_target = input("How many loops?")
    # Loop through the numbers. (Be sure to cast the string into an integer.)
    while loop_number < int(loop_target):
        # Print each number in the range
        print(loop_number)
        loop_number = loop_number + 1

    # Once complete...
    user_play = input("Continue: (y)es or (n)o? ")