import random

points = 0
crops_list = ['Bamboo', 'Bean', 'Carrot', 'Corn', 'SFlower', 'Wheat']
crops = []
global end_game

def start_game():
    print("""
        Crops:
        -> Bamboo
        -> Bean
        -> Carrot
        -> Corn
        -> SunFlower
        -> Wheat""")
    
    global end_game
    end_game = False

    crops.clear()

    for i in range(4):
        crops.append(crops_list[i])

    matrix = [[random.choice(crops) for _ in range(7)] for _ in range(5)]

    global points
    points = 0

    while not end_game:
        print_board(matrix, points)
        decision = decide()
        if decision == 'swap':
            matrix, points = swap_column(matrix, points)
        elif decision == 'reset':
            matrix, points = reset_board(matrix, points)

    while True:
        print("""
            Play again?
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

def print_board(matrix, points):
    print(f'\nPoints: {points}')

    for row_idx, row in enumerate(matrix):
        print(f'Row{row_idx+1} |\t\t\t' + '\t\t\t'.join(map(str, row)))

    print('\t\t\t'.join(['------'] * 8))

    column_labels = [f'Col{i+1}' for i in range(len(matrix[0]))]
    print('\t\t\t' + '\t\t\t'.join(column_labels))

def swap_column(matrix, points):
    while True:
        try:
            print("\n\tColumn to swap:")
            col_1 = int(input("\tEnter column 1 (1-7): ")) - 1
            col_2 = int(input("\tEnter column 2 (1-7): ")) - 1

            if col_1 not in range(7) or col_2 not in range(7):
                print("Invalid input! Columns must be between 1 and 7.")
                print_board(matrix, points)
                continue

            if col_1 == col_2:
                print("Invalid input! You cannot swap the same column.")
                print_board(matrix, points)
                continue

            for row in matrix:
                row[col_1], row[col_2] = row[col_2], row[col_1]

            print()
            points = check_connections(matrix, points)
            return matrix, points
        
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            print_board(matrix, points)

def check_connections(matrix, points):
    success = False
    check_points(points)
    
    for row_idx, row in enumerate(matrix):
        current_crop = row[0]
        state = 0
        
        for i in range(len(row)):
            if row[i] == current_crop:
                state += 1
            else:
                if state == 3:
                    points += 1
                    success = True
                    print(f"Connection of 3 '{current_crop}' crops found in row {row_idx+1}!")
                    replace(row, i - state, state)
                elif state == 5:
                    points += 3
                    success = True
                    print(f"Connection of {state} '{current_crop}' crops found in row {row_idx+1}!")
                    replace(row, i - state, state)
                elif state == 6:
                    points += 5
                    success = True
                    print(f"Connection of {state} '{current_crop}' crops found in row {row_idx+1}!")
                    replace(row, i - state, state)
                state = 1
                current_crop = row[i]
        
        if state == 3:
            points += 1
            success = True
            print(f"Connection of 3 '{current_crop}' crops found in row {row_idx+1}!")
            replace(row, i - state, state)
        if state == 5:
            points += 3
            success = True
            print(f"Connection of {state} '{current_crop}' crops found in row {row_idx+1}!")
            replace(row, i - state, state)
        elif state == 6:
            points += 5
            success = True
            print(f"Connection of {state} '{current_crop}' crops found in row {row_idx+1}!")
            replace(row, i - state, state)
    
    if not success:
        print("No more connections can be made. Game over!")
        global end_game
        end_game = True
    
    return points

def replace(row, start_idx, length):
    for i in range(start_idx, start_idx + length):
        row[i] = random.choice(crops)

def check_points(points):
    if points > 10 and crops_list[4] not in crops:
        crops.append(crops_list[4])
    if points > 20 and crops_list[5] not in crops:
        crops.append(crops.list[5])

def decide():
    while True:
        decision = input("\nWhat do you want to do? Type '1' to swap columns or '2' to reset the board: ")
        if decision in ['1', '2']:
            if decision == '1':
                return 'swap'
            else:
                return 'reset'
        else:
            print("Invalid decision!")

def reset_board(matrix, points):
    matrix = [[random.choice(crops) for _ in range(7)] for _ in range(5)]
    if points < 3:
        points = 0
    else:
        points -= 3

    print("Board has been reset!")
    return matrix, points