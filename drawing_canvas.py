import sys
import pygame
from pygame.locals import *

from utility_functions import get_font, displayText
from button import Button

DOUBLE_CLICK_TIME = 1
CANVAS_BACKGROUND_COLOR = "White"
TICK_TIMER = pygame.USEREVENT + 1


def drawingCanvasScreen(mainScreen):
    mousePosition = pygame.mouse.get_pos()
    timeRemaining = 60
    isDrawing = False
    drawingColor = (0, 0, 0)
    timer = pygame.time.Clock()
    
    mainScreen.fill(CANVAS_BACKGROUND_COLOR)
    drawingSurface = pygame.Surface(mainScreen.get_size())
    drawingSurface.fill(CANVAS_BACKGROUND_COLOR)
    pygame.time.set_timer(TICK_TIMER, 1000)
    
    while True:
        # Progress the internal clock to tick game timer.
        timer.tick(60)
        
        # Declare a background surface to separate the drawing layer from the text layer.
        displayText(f"Time Remaining: {timeRemaining}", (80, 20), fontSize=20, mainScreen=mainScreen, backgroundScreen=drawingSurface)
        displayText(f"Blink twice to toggle!", (620, 30), mainScreen=mainScreen, backgroundScreen=drawingSurface)
    
        # clearButtonPosition = (10, 700)
        clearButton = Button(image=None, pos=(1080, 650), text_input="Clear", font=get_font(30), base_color="Black", hovering_color="Green")
        pygame.draw.rect(drawingSurface, "Red", clearButton.rect)
        
        for button in [clearButton]:
            button.update(mainScreen)
        
        # Event loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            
            # Detects a click (human double blink) and toggles the drawing mode. 
            if event.type == pygame.MOUSEBUTTONDOWN:
                isDrawing = not isDrawing
                if not isDrawing:
                    if clearButton.checkForInput(mousePosition):
                        mainScreen.fill("White")
                        takeScreenshot(drawingSurface)
                    
                    

            # Plots a circle if the mouse is in mortion and drawing mode is active.
            if event.type == pygame.MOUSEMOTION and isDrawing:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(mainScreen, drawingColor, (pos[0], pos[1]), 5.0)
                
            # Handling TICK_TIMER event here.
            if event.type == TICK_TIMER: 
                if timeRemaining <= 0:
                    pygame.time.set_timer(TICK_TIMER, 0)
                    pass # TODO: Call the next screen here.
                else:
                    timeRemaining -= 1
            
                
                        
        pygame.display.update()


def takeScreenshot(screenshotLayer, filename="userDrawing.jpg"): pygame.image.save(screenshotLayer, filename)