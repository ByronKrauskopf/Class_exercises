# Incorporate the random library
import random


# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals

if user_choice == "r" and computer_choice == "s":
    print(f"You chose rock. The computer chooses scissors\n"
    f"Congratulations! you won.")
elif user_choice == "r" and computer_choice == "p":
    print(f"You chose rock. The computer chooses paper\n"
    f"Sorry, you lost.")
elif user_choice == "r" and computer_choice == "r":
    print(f"You chose rock. The computer chooses rock.\n"
    f"You tied")
elif user_choice == "p" and computer_choice == "s":
    print (f"you chose paper. The computer chooses scissors\n"
    f"Sorry, you lost")
elif user_choice == "p" and computer_choice == "p":
    print (f"you chose paper. The computer chooses paper\n"
    f"You tied.")
elif user_choice == "p" and computer_choice == "r":
    print(f"You chose paper. The computer chooses rock\n"
    f"Congratulations! You won.")
elif user_choice == "s" and computer_choice == "s":
    print(f"You chose scissors. The computer chooses scissors\n"
    f"You tied." )
elif user_choice == "s" and computer_choice == "p":
    print(f"You chose scissors. The computer chooses paper\n"
    f"Congratulations! You win.")
elif user_choice == "s" and computer_choice == "r":
    print(f"You chose scissors. The computer chooses rock.\n"
    f"Sorry, you lost.")


