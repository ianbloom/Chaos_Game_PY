import math
import pygame
import random


def instantiatePoints(pointCount):
    pointList = []
    for i in range(0, pointCount):
        x = math.cos(2 * math.pi * i / pointCount)
        y = math.sin(2 * math.pi * i / pointCount)

        pointList.append([x, y])

    return pointList


def pixelToCartesian(inp, WINDOWWIDTH, WINDOWHEIGHT):
    pixelX = inp[0]
    pixelY = inp[1]

    valX = (2 / WINDOWHEIGHT) * (pixelX - (WINDOWWIDTH / 2))
    valY = (-2 * WINDOWHEIGHT) * (pixelY - (WINDOWHEIGHT / 2))

    return [valX, valY]


def cartesianToPixel(inp, WINDOWWIDTH, WINDOWHEIGHT):
    x = inp[0]
    y = inp[1]

    valX = (x * WINDOWHEIGHT / 2) + (WINDOWWIDTH / 2) - 1
    valY = (y * -1 * WINDOWHEIGHT / 2) + (WINDOWHEIGHT / 2) - 1

    intX = int(round(valX))
    intY = int(round(valY))

    return [intX, intY]


def nextChoice(choices, pointCount, conditionArray):
    if choices[0] is None:
        temp = random.randint(0, pointCount - 1)
        choices[0] = temp
    else:
        temp = random.randint(0, pointCount - 1)
        idx = (temp - choices[0]) % pointCount
        if not conditionArray[idx]:
            for i in range(len(choices) - 2, -1, -1):
                choices[i + 1] = choices[i]
            choices[0] = temp
        else:
            nextChoice(choices, pointCount, conditionArray)

    return choices


def prepPoint(choices, pointList, selection):
    x = selection[0]
    y = selection[1]

    _x = (pointList[choices[0]][0] + x) / 2
    _y = (pointList[choices[0]][1] + y) / 2

    return [_x, _y]


def drawPixel(inp, pixelArray, color):
    x = inp[0]
    y = inp[1]

    pixelArray[x, y] = color


class button:
    def __init__(self, posX, posY, rectW, rectH, color, highlightColor, DISPLAYSURF):

        self.highlight = False
        self.DISPLAYSURF = DISPLAYSURF
        self.rectangle = pygame.Rect(posX, posY, rectW, rectH)
        self.color = color
        self.highlightColor = highlightColor
        self.pressed = False
        self.render()

    def mouseOver(self, mousePos):

        if self.rectangle.collidepoint(mousePos[0], mousePos[1]):
            self.highlight = True
            return True
        else:
            self.highlight = False
            return False

    def render(self, DISPLAYSURF):
        if not self.pressed:
            if self.highlight:
                pygame.draw.rect(DISPLAYSURF, self.highlightColor, self.rectangle, 0)
            if not self.highlight:
                pygame.draw.rect(DISPLAYSURF, self.color, self.rectangle, 0)
        if self.pressed:
            pygame.draw.rect(DISPLAYSURF, self.highlightColor, self.rectangle, 0)
