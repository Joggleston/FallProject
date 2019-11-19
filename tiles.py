from graphics import *

trueX = 0

difficulty = input("Beginner, Intermediate, or Expert?: ")

winX, winY = 400, 400

win = GraphWin("Minesweeper", winX, winY)
win.setBackground(color_rgb(130, 70, 70))

if difficulty.lower()[0] == "b":
    tileX, tileY = winX/8, winY/8
    x, y = 8, 8
if difficulty.lower()[0] == "i":
    tileX, tileY = winX/16, winY/16
    x, y = 16, 16
if difficulty.lower()[0] == "e":
    tileX, tileY = winX/16, winY/30
    x, y = 16, 30
    

rect = Rectangle(Point(0, 0), Point(tileX-tileX/8, tileY-tileY/8))
rect.setFill(color_rgb(225, 225, 225))
rect.setOutline(color_rgb(225, 225, 225))

bevelV = Rectangle(Point(tileX-tileX/8, tileY/8), Point(tileX, tileY-tileY/8))
bevelV.setFill(color_rgb(240, 240, 240))
bevelV.setOutline(color_rgb(240, 240, 240))

cornerV1 = Polygon(Point(tileX-tileX/8, 0), Point(tileX-tileX/8, tileY/8), Point(tileX, tileY/8))
cornerV1.setFill(color_rgb(240, 240, 240))
cornerV1.setOutline(color_rgb(240, 240, 240))

cornerV2 = Polygon(Point(tileX-tileX/8, tileY-tileY/8), Point(tileX, tileY-tileY/8), Point(tileX, tileY))
cornerV2.setFill(color_rgb(240, 240, 240))
cornerV2.setOutline(color_rgb(240, 240, 240))


bevelH = Rectangle(Point(tileX/8, tileY-tileY/8), Point(tileX-tileX/8, tileY))
bevelH.setFill(color_rgb(175, 175, 175))
bevelH.setOutline(color_rgb(175, 175, 175))

cornerH1 = Polygon(Point(0, tileY-tileY/8), Point(tileX/8, tileY-tileY/8), Point(tileX/8, tileY))
cornerH1.setFill(color_rgb(175, 175, 175))
cornerH1.setOutline(color_rgb(175, 175, 175))

cornerH2 = Polygon(Point(tileX-tileX/8, tileY-tileY/8), Point(tileX-tileX/8, tileY), Point(tileX, tileY))
cornerH2.setFill(color_rgb(175, 175, 175))
cornerH2.setOutline(color_rgb(175, 175, 175))

split = Line(Point(tileX-tileX/8, tileY-tileY/8), Point(tileX, tileY))
split.setOutline(color_rgb(150, 150, 150))

rect.draw(win)
bevelV.draw(win)
cornerV1.draw(win)
cornerV2.draw(win)
bevelH.draw(win)
cornerH1.draw(win)
cornerH2.draw(win)
split.draw(win)

cloned = rect
cloned2 = bevelV
cloned3 = cornerV1
cloned4 = cornerV2
cloned5 = bevelH
cloned6 = cornerH1
cloned7 = cornerH2
cloned8 = split

for i in range(y):
    if i > 0:
        cloned.move(tileY, -tileX*y)
        cloned2.move(tileY, -tileX*y)
        cloned3.move(tileY, -tileX*y)
        cloned4.move(tileY, -tileX*y)
        cloned5.move(tileY, -tileX*y)
        cloned6.move(tileY, -tileX*y)
        cloned7.move(tileY, -tileX*y)
        cloned8.move(tileY, -tileX*y)
    for j in range(x):
        if x == 0:
            cloned = rect
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    for j in range(x):
        if x == 0:
            cloned2 = bevelV
        cloned2 = cloned2.clone()
        cloned2.move(trueX, tileY)
        cloned2.draw(win)

    for j in range(x):
        if x == 0:
            cloned3 = cornerV1
        cloned3 = cloned3.clone()
        cloned3.move(trueX, tileY)
        cloned3.draw(win)

    for j in range(x):
        if x == 0:
            cloned4 = cornerV2
        cloned4 = cloned4.clone()
        cloned4.move(trueX, tileY)
        cloned4.draw(win)

    for j in range(x):
        if x == 0:
            cloned5 = bevelH
        cloned5 = cloned5.clone()
        cloned5.move(trueX, tileY)
        cloned5.draw(win)

    for j in range(x):
        if x == 0:
            cloned = cornerH1
        cloned6 = cloned6.clone()
        cloned6.move(trueX, tileY)
        cloned6.draw(win)

    for j in range(x):
        if x == 0:
            cloned7 = cornerH2
        cloned7 = cloned7.clone()
        cloned7.move(trueX, tileY)
        cloned7.draw(win)

    for j in range(x):
        if x == 0:
            cloned8 = split
        cloned8 = cloned8.clone()
        cloned8.move(trueX, tileY)
        cloned8.draw(win)
