import random, pygame, sys
from pygame.locals import *
import math

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 1024 # size of window's width in pixels
WINDOWHEIGHT = 768 # size of windows' height in pixels

YMAX = 1 # Set the y-axis of cartesian coordinates to coorespond to the windowheight
XMAX = WINDOWWIDTH / WINDOWHEIGHT * YMAX # Set the x-axis so that coordinates are square

selectionInput = []

# pointCount = 8

BLACK = (0,0,0)
WHITE = (255,255,255,255)
LIGHTPURPLE = (255,100,255,255)
BACKGROUND = (0,0,0)

buttonCount = 10
buttonGap = 10
buttonWidth = 40
buttonHeight = 40

buttonMargin = (WINDOWWIDTH - (buttonWidth * 10 + buttonGap * 9)) // 2

# Flag that will trigger the rendering of the Chaos Game
runFlag = False

def menu():
    global FPSCLOCK, DISPLAYSURF, runFlag, selectionInput
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill((0,0,0))

    # These arrays hold the generator point array, selection array, and run button array respectively
    buttonArray = []
    secondButtonArray = []
    runButtonArray = []

    # Initialize variables for title
    titleFont = pygame.font.Font("ostrich-regular.ttf", 72)
    titleSize = titleFont.size('Chaos Game')
    titleLocation = ((WINDOWWIDTH - titleSize[0]) // 2, (WINDOWHEIGHT - titleSize[1]) // 4)
    titleRect = pygame.Rect(titleLocation[0], titleLocation[1], titleSize[0], titleSize[1])

    # Initialize variables for credits
    creditFont = pygame.font.Font("ostrich-regular.ttf", 48)
    creditSize = creditFont.size('by Ian Bloom')
    creditLocation = ((WINDOWWIDTH - creditSize[0]) // 2, titleRect.bottom + 5)
    creditRect = pygame.Rect(creditLocation[0], creditLocation[1], creditSize[0], creditSize[1])

    # Initialize text objects to hold information about both title and credits
    TEST = Color(200,255,200,0)
    title = text("Chaos Game", titleFont, TEST)
    credit = text("by Ian Bloom", creditFont, TEST)

    for i in range(0, buttonCount):
        testButton = button(buttonMargin + (buttonWidth * i) + (buttonGap * i), WINDOWHEIGHT // 2, buttonWidth, buttonHeight, WHITE, LIGHTPURPLE)
        buttonArray.append(testButton)



    # Initialize Counter
    tick = 0

    circleColor = (255,0,0,255)
    ## Game Loop ##
    while True:
        if runFlag == True:
            break
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Loop to capture mouseover events of buttons and highlighting
            if pygame.time.get_ticks() > 5000:
                for item in buttonArray:
                    item.mouseOver(mousePos)
                for item in secondButtonArray:
                    item.mouseOver(mousePos)
                for item in runButtonArray:
                    item.mouseOver(mousePos)
            # Loop to detect button clicks for 
            if event.type == MOUSEBUTTONUP and pygame.time.get_ticks() > 5000:
                for idx, item in enumerate(buttonArray):
                    if item.mouseOver(mousePos) == True:
                        if item.pressed == False:
                            for thing in buttonArray:
                                thing.pressed = False
                            item.pressed = True
                            secondButtonArray = []
                            runButtonArray = []
                            selectionInput = []
                            for i in range(0, idx + 1):
                                testButton = button(buttonMargin + (buttonWidth * i) + (buttonGap * i), (WINDOWHEIGHT // 2) + buttonHeight + buttonGap, buttonWidth, buttonHeight, WHITE, LIGHTPURPLE)
                                secondButtonArray.append(testButton)
                                selectionInput.append(False)
                            ### Added in the RUN BUTTON here ###
                            runButton = button((WINDOWWIDTH // 2) - buttonWidth * 2.5, (WINDOWHEIGHT // 2) + 2 * buttonHeight + 3 * buttonGap, buttonWidth * 5, buttonHeight, WHITE, LIGHTPURPLE)
                            runButtonArray.append(runButton)
                        elif item.pressed == True:
                            item.pressed = False
                            secondButtonArray = []
                for idx, item in enumerate(secondButtonArray):
                    if item.mouseOver(mousePos) == True:
                        if item.pressed == False:
                            item.pressed = True
                            selectionInput[idx] = True
                        elif item.pressed == True:
                            item.pressed = False
                            selectionInput[idx] = False
                for idx, item in enumerate(runButtonArray):
                    if item.mouseOver(mousePos) == True:
                        if item.pressed == False:
                            item.pressed = True
                            runFlag = True
                        elif item.pressed == True:
                            item.pressed = False
                            runFlag = False


        if(pygame.time.get_ticks() < 4000):

            DISPLAYSURF.fill(BACKGROUND) # Fill the display surface with background color (BLACK)
            TEXTCOLOR = Color(255,255,255,255)
            #TEXTCOLOR = Color(255 * (math.cos(tick) + 1) // 2, 128, 255, 255) # Update text color (fades between pinkish and tealish)

            # Change title color
            title.color = TEXTCOLOR
            title.render()
            title.selfBlit()

            # Change credit color
            credit.color = TEXTCOLOR
            credit.render()
            credit.selfBlit()

            tick += .005 # tick for Counter

            DISPLAYSURF.blit(title.surface, (titleLocation[0], titleLocation[1])) # Copy surface containing title text element to display surface at titleLocation
            DISPLAYSURF.blit(credit.surface, (creditLocation[0] , creditLocation[1])) # Copy surface containing credit text element to display surface at creditLocation

            pygame.display.update()
            FPSCLOCK.tick(FPS)

        if(pygame.time.get_ticks() >= 3000 and pygame.time.get_ticks() < 5000):

            DISPLAYSURF.fill(BACKGROUND) # Fill the display surface with background color (BLACK) 

            tick += .005

            # Change title color
            title.color = TEXTCOLOR
            title.render()
            title.selfBlit()

            # Change credit color
            credit.color = TEXTCOLOR
            credit.render()
            credit.selfBlit()

            while(credit.surface.get_alpha() > 0):

                DISPLAYSURF.fill(BACKGROUND)
                # Change title color
                title.color = TEXTCOLOR
                title.render()
                title.selfBlit()

                # Change credit color
                credit.color = TEXTCOLOR
                credit.render()
                credit.selfBlit()

                credit.surface.set_alpha(credit.surface.get_alpha() - 5)

                tick += .005 # tick for Counter

                DISPLAYSURF.blit(title.surface, (titleLocation[0], titleLocation[1])) # Copy surface containing title text element to display surface at titleLocation
                DISPLAYSURF.blit(credit.surface, (creditLocation[0] , creditLocation[1])) # Copy surface containing credit text element to display surface at creditLocation

                pygame.display.update()
                FPSCLOCK.tick(FPS)

        if(pygame.time.get_ticks() >= 4000):
            
            DISPLAYSURF.fill(BACKGROUND)

            # Change title color
            title.color = WHITE
            title.render()
            title.selfBlit()

            for item in buttonArray:
                item.render()
            for idx, item in enumerate(secondButtonArray):
                item.render()
                # selectionInput[idx] = item.pressed
            for item in runButtonArray:
                item.render()

            # testButton.render()

            DISPLAYSURF.blit(title.surface, (titleLocation[0], titleLocation[1])) # Copy surface containing title text element to display surface at titleLocation

            tick += .005 # tick for Counter

            pygame.display.update()
            FPSCLOCK.tick(FPS)
    mainLoop(len(secondButtonArray), selectionInput)


class text:

    def __init__(self, string, font, color):

        self.string = str(string)
        textSize = font.size(string)
        self.surface = pygame.Surface(textSize)
        self.surface.set_alpha(255)
        self.color = color
        self.font = font
        self.renderSurf = self.font.render(self.string, True, self.color)
        self.width = self.renderSurf.get_width()
        self.height = self.renderSurf.get_height()

    def render(self):

        self.renderSurf = self.font.render(self.string, True, self.color)

    def selfBlit(self):

        self.surface.blit(self.renderSurf, (0,0))

class button:

    global DISPLAYSURF

    def __init__(self, posX, posY, rectW, rectH, color, highlightColor):

        self.highlight = False
        self.rectangle = Rect(posX, posY, rectW, rectH)
        self.color = color
        self.highlightColor = highlightColor
        self.pressed = False
        self.render()

    def mouseOver(self, mousePos):

        if self.rectangle.collidepoint(mousePos[0], mousePos[1]) == True:
            self.highlight = True
            return True
        else:
            self.highlight = False
            return False

    def render(self):
        if self.pressed == False:
            if self.highlight == True:
                pygame.draw.rect(DISPLAYSURF, self.highlightColor, self.rectangle, 0)
            if self.highlight == False:
                pygame.draw.rect(DISPLAYSURF, self.color, self.rectangle, 0)
        if self.pressed == True:
            pygame.draw.rect(DISPLAYSURF, self.highlightColor, self.rectangle, 0)

def mainLoop(pointCount, selectionInput):
    global FPSCLOCK, DISPLAYSURF, WINDOWWIDTH, WINDOWHEIGHT, runFlag
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill(BLACK)
    pixelArray = pygame.PixelArray(DISPLAYSURF)

    memoryLength = 3 # how many choices will we remember

    choices = [] # initialize our choices array which will hold points in memory
    for i in range(memoryLength):
        choices.append(None)


    pointsArray = instantiatePoints(pointCount)
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Chaos Game')

    selection = [random.uniform(-1,1), random.uniform(-1,1)] # first point in iterative process is randomly selected w/in unit square
    drawFlag = False

    exitButton = button(WINDOWWIDTH - buttonWidth - buttonGap, buttonGap, buttonWidth, buttonHeight, WHITE, LIGHTPURPLE)

    while True:
        if runFlag == False:
            break
        # Loop to draw points in pointsArray
        for item in pointsArray:
            item = cartesianToPixel(item)
            #drawPixel(item,pixelArray)
            pygame.draw.circle(DISPLAYSURF, WHITE, item, 2, 0)

        for i in range (0,1000):
            #temp = nextChoice(choices, pointCount, [False, False, False, True, False, True, True, True])
            temp = nextChoice(choices, pointCount, selectionInput)
            choices = temp

            cart = prepPoint(choices, pointsArray, selection)
            selection = cart
            pixel = cartesianToPixel(selection)
            if drawFlag == True:
                drawPixel(pixel, pixelArray)

        drawFlag = True

        # Render exit button
        exitButton.render()

        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get(): # event handling loop
            exitButton.mouseOver(mousePos)
            if event.type == MOUSEBUTTONUP:
                if exitButton.mouseOver(mousePos) == True:
                    if exitButton.pressed == False:
                        exitButton.pressed = True
                        runFlag = False
                        break
                    elif exitButton.pressed == True:
                        exitButton.pressed = False
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    # Reset ALL THE THINGS
    del pixelArray
    buttonArray = []
    secondButtonArray = []
    runButtonArray = []
    menu()


def pixelToCartesian(inp):
    global WINDOWWIDTH, WINDOWHEIGHT

    pixelX = inp[0]
    pixelY = inp[1]

    valX = (2 / WINDOWHEIGHT) * (pixelX - (WINDOWWIDTH / 2))
    valY = (-2 * WINDOWHEIGHT) * (pixelY - (WINDOWHEIGHT / 2))

    return [valX, valY]

def cartesianToPixel(inp):
    global WINDOWWIDTH, WINDOWHEIGHT

    x = inp[0]
    y = inp[1]

    valX = (x * WINDOWHEIGHT / 2) + (WINDOWWIDTH / 2) - 1
    valY = (y * -1 * WINDOWHEIGHT / 2) + (WINDOWHEIGHT / 2) - 1

    intX = int(round(valX))
    intY = int(round(valY))
    
    return [intX, intY]

def instantiatePoints(pointCount):
    pointList = []
    for i in range(0,pointCount):
        x = math.cos(2 * math.pi * i / pointCount)
        y = math.sin(2 * math.pi * i / pointCount)

        pointList.append([x,y])

    return pointList

def nextChoice(choices, pointCount, conditionArray):
    if choices[0] == None:
        temp = random.randint(0, pointCount - 1)
        choices[0] = temp
    else:
        temp = random.randint(0, pointCount - 1)
        idx = (temp - choices[0]) % pointCount
        if conditionArray[idx] != True:
            for i in range(len(choices) - 2,-1,-1):
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

def drawPixel(inp, pixelArray):
    x = inp[0]
    y = inp[1]

    pixelArray[x,y] = WHITE

###
###
###

### BEGIN THE PROGRAM ###

###
###
###

menu()