import subprocess
import platform

def sum_values(a, b, c):
    return a + b + c

def clearConsole():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"], shell=True)

def printBoard(xState, zState):
    board = []
    for i in range(9):
        if xState[i]:
            board.append('X')
        elif zState[i]:
            board.append('O')
        else:
            board.append(i)
    
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]}") 

def checkWin(xState, zState):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:  
        if(sum_values(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X won the game!")
            return 1
        if(sum_values(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O won the game!")
            return 0
    if sum(xState) + sum(zState) == 9:
        print("It's a Tie!")
        return 2
    return -1

if __name__ == "__main__":
    while True:
        xState = [0] * 9
        zState = [0] * 9
        turn = 1
        clearConsole()
        print("Welcome to Tic Tac Toe")
        
        while True:
            printBoard(xState, zState)
            try:
                player_char = "X" if turn == 1 else "O"
                print(f"{player_char}'s turn")
                inp = input("Enter a number or 'q' to quit: ").lower()
                
                if inp == 'q':
                    exit()
                
                value = int(inp)

                if xState[value] == 1 or zState[value] == 1:
                    clearConsole()
                    print("⚠️ That place is already taken!")
                    continue 

                if turn == 1:
                    xState[value] = 1
                else:
                    zState[value] = 1

            except (ValueError, IndexError):
                clearConsole()
                print("❌ Invalid input! Enter 0-8.")
                continue

            clearConsole()
            win = checkWin(xState, zState)
            if win != -1:
                printBoard(xState, zState)
                print("Game Over")
                input("Press any key to exit")
                break
            turn = 1 - turn

        retry = input("Press 'r' to restart or any other key to quit: ").lower()
        if retry != 'r':
            print("Thanks for playing!")
            break