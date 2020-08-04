import random
from time import sleep

board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def Board(board):
    print('\n\n\t\t\t            |              |                 ')
    print('\t\t\t     ', board[1], '    |      ', board[2], '     |    ', board[3])
    print('\t\t\t            |              |                 ')
    print('\t\t\t------------+--------------+------------')
    print('\t\t\t            |              |                 ')
    print('\t\t\t     ', board[4], '    |      ', board[5], '     |    ', board[6])
    print('\t\t\t            |              |               ')
    print('\t\t\t------------+--------------+------------')
    print('\t\t\t            |              |                 ')
    print('\t\t\t     ', board[7], '    |      ', board[8], '     |    ', board[9])
    print('\t\t\t            |              |               \n\n')


def checkWinO(board):
    if board[1] == board[2] == board[3] == '𝕆' or board[4] == board[5] == board[6] == '𝕆' or board[7] == board[8] == \
            board[9] == '𝕆':
        return True
    elif board[1] == board[4] == board[7] == '𝕆' or board[5] == board[2] == board[8] == '𝕆' or board[6] == board[9] == \
            board[3] == '𝕆':
        return True
    elif board[1] == board[5] == board[9] == '𝕆' or board[7] == board[5] == board[3] == '𝕆':
        return True
    else:
        return False


def checkWinX(board):
    if board[1] == board[2] == board[3] == '𝕏' or board[4] == board[5] == board[6] == '𝕏' or board[7] == board[8] == \
            board[9] == '𝕏':
        return True
    elif board[1] == board[4] == board[7] == '𝕏' or board[5] == board[2] == board[8] == '𝕏' or board[6] == board[9] == \
            board[3] == '𝕏':
        return True
    elif board[1] == board[5] == board[9] == '𝕏' or board[3] == board[5] == board[7] == '𝕏':
        return True
    else:
        return False


def easy(board, name):
    flag=1
    while flag:
        first = random.randint(0, 1)
        cnt = 0
        if first == 0:
            Board(board)
            print("It's computers turn. Please wait ....")
            sleep(2)
            n = random.randint(1, 9)
            while board[n] != ' ':
                n = random.randint(1, 9)
            board[n] = '𝕆'
            cnt = 1
            first = 1
        while checkWinO(board) == checkWinX(board) == False and cnt < 9:
            first = first % 2
            if first == 0:
                Board(board)
                print("It's computers turn. Please wait ....")
                sleep(2)
                n = random.randint(1, 9)
                while board[n] != ' ':
                    n = random.randint(1, 9)
                board[n] = '𝕆'
            else:
                Board(board)
                n = int(input(name.upper() + "(𝕏) It's your turn please enter a number: -\t"))
                while n not in board or board[n] != ' ':
                    n = int(input("\nIt's not a valid move please enter again: -\t"))
                board[n] = '𝕏'
            first += 1
            cnt += 1
        if checkWinX(board):
            Board(board)
            print('\nCongratulations ' + name.upper() + "(X) has won.")
        elif checkWinO(board):
            Board(board)
            print("\nOops COMPUTER(O) has won.")
        else:
            Board(board)
            print("\nIt's a tie.")
        print('\nThe game has ended.')
        while 1:
            print('\n0. Exit\t\t\t\t\t\t\t1. Play Again')
            flag = int(input('\nEnter your choice: -\t'))
            if flag in (0, 1):
                break
            else:
                print('\nNot a valid choice, Please enter again.')
        board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def standard(board, name):
    flag = 1
    while flag:
        first = random.randint(0, 1)
        cnt = 0
        if first == 0:
            Board(board)
            print("It's computers turn. Please wait ....")
            sleep(2)
            n = random.randint(1, 9)
            while board[n] != ' ':
                n = random.randint(1, 9)
            board[n] = '𝕆'
            cnt = 1
            first = 1
        while checkWinO(board) == checkWinX(board) == False and cnt < 9:
            first = first % 2
            if first == 0:
                Board(board)
                print("It's computers turn. Please wait ....")
                sleep(2)
                n = random.randint(1, 9)
                while board[n] != ' ':
                    n = random.randint(1, 9)
                board[n] = '𝕆'
            else:
                Board(board)
                n = int(input(name.upper() + "(𝕏) It's your turn please enter a number: -\t"))
                while n not in board or board[n] != ' ':
                    n = int(input("\nIt's not a valid move please enter again: -\t"))
                board[n] = '𝕏'
            first += 1
            cnt += 1
        if checkWinX(board):
            Board(board)
            print('\nCongratulations ' + name.upper() + "(X) has won.")
        elif checkWinO(board):
            Board(board)
            print("\nOops COMPUTER(O) has won.")
        else:
            Board(board)
            print("\nIt's a tie.")
        print('\nThe game has ended.')
        while 1:
            print('\n0. Exit\t\t\t\t\t\t\t1. Play Again')
            flag = int(input('\nEnter your choice: -\t'))
            if flag in (0, 1):
                break
            else:
                print('\nNot a valid choice, Please enter again.')
        board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}


def soloplayer(board):
    print("\n\n\t\t\tTwo types of levels are\t")
    while 1:
        print('\n1. Easy\t\t\t\t\t\t\t2. Standard\n')
        level = int(input("Please enter your choice: -\t"))
        if level in (1, 2):
            break
        else:
            print('\nNot a valid choice, Please enter again.')
    name = input("\nPlease enter  your name (𝕏): -\t")
    easy(board, name) if level == 1 else standard(board, name)


def multiplayer(board):
    names, cnt, flag = [], 0, 1
    mark = ['𝕏', '𝕆']
    for i in range(2):
        name = input('\nName of player {}: -\t'.format(i + 1))
        names += [name]
    while flag:
        first = random.randint(0, 1)
        while checkWinO(board) == checkWinX(board) == False and cnt < 9:
            first = first % 2
            Board(board)
            n = int(input(names[first].upper() + ' (' + mark[first] + ") It's your turn please enter a number: -\t"))
            while n not in board or board[n] != ' ':
                n = int(input("\nIt's not a valid move please enter again: -\t"))
            board[n] = mark[first]
            cnt += 1
            first += 1
        if checkWinX(board):
            Board(board)
            print('\nCongratulations ' + names[0].upper() + "(X) has won.")
        elif checkWinO(board):
            Board(board)
            print('\nCongratulations ' + names[1].upper() + "(O) has won.")
        else:
            Board(board)
            print("\nIt's a tie.")
        print('\nThe game has ended.')
        while 1:
            print('\n0. Exit\t\t\t\t\t\t\t1. Play Again')
            flag = int(input('\nEnter your choice: -\t'))
            if flag in (0, 1):
                break
            else:
                print('\nNot a valid choice, Please enter again.')
        board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        cnt = 0


print('\t\t\t\t\t\t𝐓𝐢𝐜 𝐓𝐚𝐜 𝐓𝐨𝐞\n\n\n')
print('Modes: -\n\n')
while 1:
    print('1. SoloPlayer\t\t\t\t\t\t\t2. MultiPlayer\n')
    mode = int(input('Enter a number to select a mode: -\t'))
    if mode in (1, 2):
        break
    else:
        print('\nNot a valid mode, Please select again.\n')
multiplayer(board) if mode == 2 else soloplayer(board)
