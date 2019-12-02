from graphics import *
import os
import random

winX, winY = 400, 500   
win = GraphWin("Minesweeper", winX, winY)
win.setBackground(color_rgb(70, 170, 170))

def main():
    difficulty(winX, winY)  
            
def difficulty(winX, winY):

    prompt = Text(Point(winX/2, winY/9), "Select the difficulty")
    prompt.setFill(color_rgb(50, 50, 50))
    prompt._reconfig("font", ("Courier New", 20, "italic"))
    prompt.draw(win)

                  
    B = Rectangle(Point(winX/6, winY/6), Point(winX-winX/6, 2*winY/6))
    B.setFill(color_rgb(200, 200, 200))
    B.draw(win)

    I = Rectangle(Point(winX/6, 2.5*winY/6), Point(winX-winX/6, 3.5*winY/6))
    I.setFill(color_rgb(200, 200, 200))
    I.draw(win)

    E = Rectangle(Point(winX/6, 4*winY/6), Point(winX-winX/6, 5*winY/6))
    E.setFill(color_rgb(200, 200, 200))
    E.draw(win)

    txtB = Text(Point(winX/2, winY/4), "Beginner")
    txtB.setFill(color_rgb(50, 50, 50))
    txtB._reconfig("font", ("Courier New", 24, "bold"))
    txtB.draw(win)

    txtI = Text(Point(winX/2, winY/2), "Intermediate")
    txtI.setFill(color_rgb(50, 50, 50))
    txtI._reconfig("font", ("Courier New", 24, "bold"))
    txtI.draw(win)

    txtE = Text(Point(winX/2, 3*winY/4), "Expert")
    txtE.setFill(color_rgb(50, 50, 50))
    txtE._reconfig("font", ("Courier New", 24, "bold"))
    txtE.draw(win)

    click = win.getMouse()
    x, y = click.getX(), click.getY()
    if click:
        prompt.undraw()
        B.undraw()
        I.undraw()
        E.undraw()
        txtB.undraw()
        txtI.undraw()
        txtE.undraw()
    if winX/6 <= x <= winX-winX/6 and winY/6 <= y <= 2*winY/6:
        diff = "beginner"
        startgame(diff)
    if winX/6 <= x <= winX-winX/6 and 2.5*winY/6 <= y <= 3.5*winY/6:
        startgame("intermediate")
    if winX/6 <= x <= winX-winX/6 and 4*winY/6 <= y <= 5*winY/6:
        startgame("expert")

def startgame(diff):
    
    board = mines()
    if diff == "beginner":
        x, y = 8, 8
        defX, defY = winX/8, winY/10    
        root = 'C:/Users/Johnathan/Desktop/comp sci work/PROJECT'
        tile = ["tilenew.png", "mine.png", "flagged.png"]
        tiles = maketiles(root, tile, defX, defY, x, y)
        
        state = [[0 for i in range(x)] for j in range(y)] #0 -> unflipped, 1 -> flipped, 2 -> flagged
         
        for j in range(y):
            for i in range(x):
                tiles[i][j].draw(win)
        #mines()
        numbers = [[Text(Point(tiles[j][i].getAnchor().getX(), tiles[j][i].getAnchor().getY()), board[j][i]) for i in range(x)] for j in range(y)]

        for i in range(y):
            for j in range(x):
                numbers[j][i]._reconfig("font", ("Courier New", 24, "bold"))
        
    while True:
        select = win.checkMouse()
        if select:
            selX, selY = select.getX(), select.getY()
            xy = []
            for i in range(y):
                for j in range(x):
                    newX = tiles[j][i].getAnchor().getX()
                    newY = tiles[j][i].getAnchor().getY()
                    if state[j][i] == 0:
                        if newX - 25 <= selX <= newX + 25 and newY - 25 <= selY <= newY + 25:
                            tiles[j][i].undraw()
                            state[j][i] = 1
                            if board[j][i] > 0:
                                numbers[j][i].draw(win)
                            if board[j][i] == -1:
                                Image(Point(newX, newY), os.path.join(root, tile[1])).draw(win)
                                #Lose
                            if board[j][i] == 0:
                               checkzero(j, i, tiles, board, state, numbers)
                               for m in range(j-1, j+2):
                                   for n in range(i-1, i+2):
                                       if board[m][n] == 0 and state[m][n] == 0:
                                           checkzero(m, n, tiles, board, state, numbers)
                                       
                               
def maketiles(z, z1, z2, z3, x, y):
    
    tiles = [[Image(Point(z2*i+z3/2, 125+z3*j), os.path.join(z, z1[0])) for i in range(x)] for j in range(y)]
    return tiles

def mines():
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
    print(board)
    return board

def checkzero(X_, Y_, tiles, board, state, numbers):
    
    if X_ is not 0 and X_ is not 7 and Y_ is not 0 and Y_ is not 7:
        for i in range(X_-1, X_+2):
            for j in range(Y_-1, Y_+2):
                tiles[i][j].undraw()
                if numbers[i][j] not "0":
                    numbers[i][j].draw(win)
                state[i][j] = 1
    elif X_ == 0:
        if Y_ == 0:
            for i in range(X_, X_+2):
                for j in range(Y_, Y_+2):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
        elif Y_ == 7:
            for i in range(X_, X_+2):
                for j in range(Y_-1, Y_+1):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
        else:
            for i in range(X_, X_+2):
                for j in range(Y_-1, Y_+2):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
    elif X_ == 7:
        if Y_ == 0:
            for i in range(X_, X_-1, -1):
                for j in range(Y_, Y_+2):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
        elif Y_ == 7:
            for i in range(X_, X_-1, -1):
                for j in range(Y_-1, Y_+1):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
        else:
            for i in range(X_, X_-1, -1):
                for j in range(Y_-1, Y_+2):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
    else:
        if Y_ == 0:
            for i in range(X_-1, X_+2):
                for j in range(Y_, Y_+2):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
        elif Y_ == 7:
            for i in range(X_-1, X_+2):
                for j in range(Y_-1, Y_+1):
                    tiles[i][j].undraw()
                    if numbers[i][j] not "0":
                        numbers[i][j].draw(win)
                    state[i][j] = 1
       
if __name__ == "__main__":
    main()
