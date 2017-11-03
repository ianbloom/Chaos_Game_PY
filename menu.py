"""
The menu

"""
import pygame


class Menu:
    def __init__(self):
        pass

    def run(self):
        global FPSCLOCK, DISPLAYSURF, runFlag, selectionInput
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        DISPLAYSURF.fill((0, 0, 0))

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
        TEST = Color(200, 255, 200, 0)
        title = text("Chaos Game", titleFont, TEST)
        credit = text("by Ian Bloom", creditFont, TEST)

        for i in range(0, buttonCount):
            testButton = button(buttonMargin + (buttonWidth * i) + (buttonGap * i), WINDOWHEIGHT // 2, buttonWidth,
                                buttonHeight, WHITE, LIGHTPURPLE)
            buttonArray.append(testButton)

        # Initialize Counter
        tick = 0

        circleColor = (255, 0, 0, 255)
        # Game Loop
        while True:
            if runFlag:
                break
            mousePos = pygame.mouse.get_pos()
            for event in pygame.event.get():  # event handling loop
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
                        if item.mouseOver(mousePos):
                            if not item.pressed:
                                for thing in buttonArray:
                                    thing.pressed = False
                                item.pressed = True
                                secondButtonArray = []
                                runButtonArray = []
                                selectionInput = []
                                for i in range(0, idx + 1):
                                    testButton = button(buttonMargin + (buttonWidth * i) + (buttonGap * i),
                                                        (WINDOWHEIGHT // 2) + buttonHeight + buttonGap, buttonWidth,
                                                        buttonHeight, WHITE, LIGHTPURPLE)
                                    secondButtonArray.append(testButton)
                                    selectionInput.append(False)
                                ### Added in the RUN BUTTON here ###
                                runButton = button((WINDOWWIDTH // 2) - buttonWidth * 2.5,
                                                   (WINDOWHEIGHT // 2) + 2 * buttonHeight + 3 * buttonGap, buttonWidth * 5,
                                                   buttonHeight, WHITE, LIGHTPURPLE)
                                runButtonArray.append(runButton)
                            elif item.pressed:
                                item.pressed = False
                                secondButtonArray = []
                    for idx, item in enumerate(secondButtonArray):
                        if item.mouseOver(mousePos):
                            if not item.pressed:
                                item.pressed = True
                                selectionInput[idx] = True
                            elif item.pressed:
                                item.pressed = False
                                selectionInput[idx] = False
                    for idx, item in enumerate(runButtonArray):
                        if item.mouseOver(mousePos):
                            if not item.pressed:
                                item.pressed = True
                                runFlag = True
                            elif item.pressed:
                                item.pressed = False
                                runFlag = False

            if pygame.time.get_ticks() < 4000:
                DISPLAYSURF.fill(BACKGROUND)  # Fill the display surface with background color (BLACK)
                TEXTCOLOR = Color(255, 255, 255, 255)
                # TEXTCOLOR = Color(255 * (math.cos(tick) + 1) // 2, 128, 255, 255) # Update text color (fades between pinkish and tealish)

                # Change title color
                title.color = TEXTCOLOR
                title.render()
                title.selfBlit()

                # Change credit color
                credit.color = TEXTCOLOR
                credit.render()
                credit.selfBlit()

                tick += .005  # tick for Counter

                DISPLAYSURF.blit(title.surface, (titleLocation[0], titleLocation[
                    1]))  # Copy surface containing title text element to display surface at titleLocation
                DISPLAYSURF.blit(credit.surface, (creditLocation[0], creditLocation[
                    1]))  # Copy surface containing credit text element to display surface at creditLocation

                pygame.display.update()
                FPSCLOCK.tick(FPS)

            if 3000 <= pygame.time.get_ticks() < 5000:

                DISPLAYSURF.fill(BACKGROUND)  # Fill the display surface with background color (BLACK)

                tick += .005

                # Change title color
                title.color = TEXTCOLOR
                title.render()
                title.selfBlit()

                # Change credit color
                credit.color = TEXTCOLOR
                credit.render()
                credit.selfBlit()

                while credit.surface.get_alpha() > 0:
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

                    tick += .005  # tick for Counter

                    DISPLAYSURF.blit(title.surface, (titleLocation[0], titleLocation[
                        1]))  # Copy surface containing title text element to display surface at titleLocation
                    DISPLAYSURF.blit(credit.surface, (creditLocation[0], creditLocation[
                        1]))  # Copy surface containing credit text element to display surface at creditLocation

                    pygame.display.update()
                    FPSCLOCK.tick(FPS)

            if pygame.time.get_ticks() >= 4000:

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

                DISPLAYSURF.blit(title.surface, (titleLocation[0], titleLocation[
                    1]))  # Copy surface containing title text element to display surface at titleLocation

                tick += .005  # tick for Counter

                pygame.display.update()
                FPSCLOCK.tick(FPS)
        mainLoop(len(secondButtonArray), selectionInput)