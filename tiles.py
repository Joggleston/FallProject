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
    

rect = Rectangle(Point(0, 0), Point(tileX, tileY-tileY/8))
rect.setFill(color_rgb(225, 225, 225))
rect.setOutline(color_rgb(225, 225, 225))

bevelV = Rectangle(Point(tileX, tileY/8), Point(tileX+tileX/8, tileY-tileY/8))
bevelV.setFill(color_rgb(240, 240, 240))
bevelV.setOutline(color_rgb(240, 240, 240))

cornerV1 = Polygon(Point(tileX, 0), Point(tileX, tileY/8), Point(tileX+tileX/8, tileY/8))
cornerV1.setFill(color_rgb(240, 240, 240))
cornerV1.setOutline(color_rgb(240, 240, 240))

cornerV2 = Polygon(Point(tileX, tileY-tileY/8), Point(tileX+tileX/8, tileY-tileY/8), Point(tileX+tileX/8, tileY))
cornerV2.setFill(color_rgb(240, 240, 240))
cornerV2.setOutline(color_rgb(240, 240, 240))


bevelH = Rectangle(Point(tileX/8, tileY-tileY/8), Point(tileX, tileY))
bevelH.setFill(color_rgb(175, 175, 175))
bevelH.setOutline(color_rgb(175, 175, 175))

cornerH1 = Polygon(Point(0, tileY-tileY/8), Point(tileX/8, tileY-tileY/8), Point(tileX/8, tileY))
cornerH1.setFill(color_rgb(175, 175, 175))
cornerH1.setOutline(color_rgb(175, 175, 175))

cornerH2 = Polygon(Point(tileX, tileY-tileY/8), Point(tileX, tileY), Point(tileX+tileX/8, tileY))
cornerH2.setFill(color_rgb(175, 175, 175))
cornerH2.setOutline(color_rgb(175, 175, 175))

split = Line(Point(tileX, tileY-tileY/8), Point(tileX+tileX/8, tileY))
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

for i in range(y):
    if i > 0:
        trueX += tileX
    for i in range(x):
        if x == 0:
            cloned = rect
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = bevelV
    for i in range(x):
        if x == 0:
            cloned = bevelV
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = cornerV1
    for i in range(x):
        if x == 0:
            cloned = cornerV1
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = cornerV2
    for i in range(x):
        if x == 0:
            cloned = cornerV2
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = bevelH
    for i in range(x):
        if x == 0:
            cloned = bevelH
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = cornerH1
    for i in range(x):
        if x == 0:
            cloned = cornerH1
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = cornerH2
    for i in range(x):
        if x == 0:
            cloned = cornerH2
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)

    cloned = split
    for i in range(x):
        if x == 0:
            cloned = split
        cloned = cloned.clone()
        cloned.move(trueX, tileY)
        cloned.draw(win)
    
