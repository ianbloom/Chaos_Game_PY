import pygame
from pygame.colordict import THECOLORS as COLORS
from pygame.locals import *
import random
from .utils import instantiatePoints, button, cartesianToPixel, nextChoice, drawPixel, prepPoint
import sys


class Flam3:
    REQ_SETTINGS = ('WINDOWWIDTH', 'WINDOWHEIGHT', 'buttonWidth', 'buttonGap', 'buttonHeight')

    def __init__(self, settings_dict, pointCount, selectionInput):
        for setting in self.__class__.REQ_SETTINGS:
            assert (setting in settings_dict)
            self.settings = settings_dict

        self.pointCount = pointCount
        self.selectionInput = selectionInput

    def run(self):
        # This will set the local variables named in REQ_SETTINGS
        for setting in self.__class__.REQ_SETTINGS:
            locals[setting] = self.settings[setting]

        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        self.DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        self.DISPLAYSURF.fill(COLORS['black'])

        runFlag = False
        pixelArray = pygame.PixelArray(self.DISPLAYSURF)
        memoryLength = 3  # how many choices will we remember

        choices = []  # initialize our choices array which will hold points in memory
        for i in range(memoryLength):
            choices.append(None)

        pointsArray = instantiatePoints(self.pointCount)
        mousex = 0  # used to store x coordinate of mouse event
        mousey = 0  # used to store y coordinate of mouse event
        pygame.display.set_caption('Chaos Game')

        selection = [random.uniform(-1, 1),
                     random.uniform(-1, 1)]  # first point in iterative process is randomly selected w/in unit square
        drawFlag = False

        exitButton = button(WINDOWWIDTH - buttonWidth - buttonGap, buttonGap,
                            buttonWidth, buttonHeight, COLORS['white'], COLORS['purple2'])

        WHITE = COLORS['white']

        while True:
            if not runFlag:
                break
            # Loop to draw points in pointsArray
            for item in pointsArray:
                item = cartesianToPixel(item, WINDOWWIDTH, WINDOWHEIGHT)
                # drawPixel(item,pixelArray)
                pygame.draw.circle(self.DISPLAYSURF, WHITE, item, 2, 0)

            for i in range(0, 1000):
                # temp = nextChoice(choices, pointCount, [False, False, False, True, False, True, True, True])
                temp = nextChoice(choices, self.pointCount, self.selectionInput)
                choices = temp

                cart = prepPoint(choices, pointsArray, selection)
                selection = cart
                pixel = cartesianToPixel(selection)
                if drawFlag:
                    drawPixel(pixel, pixelArray, WHITE)

            drawFlag = True

            # Render exit button
            exitButton.render()

            mousePos = pygame.mouse.get_pos()
            for event in pygame.event.get():  # event handling loop
                exitButton.mouseOver(mousePos)
                if event.type == MOUSEBUTTONUP:
                    if exitButton.mouseOver(mousePos):
                        if not exitButton.pressed:
                            exitButton.pressed = True
                            runFlag = False
                            break
                        elif exitButton.pressed:
                            exitButton.pressed = False
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.FPSCLOCK.tick(FPS)

        # Reset ALL THE THINGS
        del pixelArray
