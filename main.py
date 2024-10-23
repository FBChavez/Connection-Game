import random
from run_game import start_game

print("""
Welcome to a fun Connect Mini-Game!

Rules and Objective: 
-> Get as many points as you can by placing 3, 5, or 6 of the same kind of crop in a row.
-> 4 and 7 of the same kind of crop in a row is an invalid connection.
-> To connect fruits, you will need to swap two columns of your choice. If you cannot make a connection when swapping, the game ends.
-> If you see that you cannot make any connections, you can reset the board by using 3 of your points.

Points: 
Connecting 3 -> 1 pt
Connecting 5 -> 3 pts
Connecting 6 -> 5 pts
Resetting board -> -3 pts""")

while True:
    print("""
        Are you ready to play?
        Input : Option
        Yes : 1
        No : 2
""")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Great! Let's start connecting.")
        start_game()
        break 
    elif choice == '2':
        print("Have a great time!")
        break 
    else:
        print("Invalid input. Please enter 1 for Yes or 2 for No.")

