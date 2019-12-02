import random

x, y = 8, 8
n = 0
board = [[0 for i in range(x)] for j in range(y)]
while n < 10:
    col = random.randint(0, y-1)
    row = random.randint(0, y-1)
    if board[row][col] != -1:
        board[row][col] = -1
        n += 1

for i in range(x):
    for j in range(y):
        if board[i][j] != -1:
            try:
                if board[i-1][j] == -1:
                    # left, none
                    board[i][j] += 1
                if board[i][j-1] == -1:
                    #none, down
                    board[i][j] += 1
                if board[i-1][j-1] == -1:
                    #left, down
                    board[i][j] += 1
                if board[i+1][j] == -1:
                    #right, none
                    board[i][j] += 1
                if board[i][j+1] == -1:
                    #none, up
                    board[i][j] += 1
                if board[i+1][j-1] == -1:
                    #right, down
                    board[i][j] += 1
                if board[i-1][j+1] == -1:
                    #left, up
                    board[i][j] += 1
                if board[i+1][j+1] == -1:
                    #right, up
                    board[i][j] += 1
            except IndexError:
                pass
        
def checkzero(X_, Y_):
    zeroes = []

    for i in range(X_-1, X_+2):
        for j in range(Y_-1, Y_+2):
            if board[i][j] == 0:
                zeroes.append((i, j))
                board[i][j].undraw()
    X_, Y_ = zeroes[0]
    print(X_, Y_)
        for i in range(X_-1, X_+2):
            for j in range(Y_-1, Y_+2):
                if board[i][j] == 0:
                    zeroes.append((i, j))
                    board[i][j].undraw()
