import sys
import pygame
from pygame.locals import *

from utility_functions import get_font

DOUBLE_CLICK_TIME = 1
CANVAS_BACKGROUND_COLOR = "White"
DRAWING_TIME_COMPLETE = pygame.USEREVENT + 1

def drawingCanvasScreen(mainScreen):
    # playMousePosition = pygame.mouse.get_pos()
    timeRemaining = 60
    isDrawing = False
    drawingColor = (0, 0, 0)
    
    mainScreen.fill(CANVAS_BACKGROUND_COLOR)
    
    while True:
        
        # Declaring text elements
        timerText = get_font(20).render(f"Time Remaining: {timeRemaining}", True, "Black")
        toggleText = get_font(40).render("Blink twice to toggle!", True, "Black")
        hideToggleText = get_font(40).render("Blink twice to toggle!", True, CANVAS_BACKGROUND_COLOR)
        
        
        # Declaring text bounding boxes
        textRect = timerText.get_rect(center=(100, 20))
        toggleRect = toggleText.get_rect(center=(640, 30)) # Same bounding box can be used for the toggle text and hide toggle text.
        
        # Blitting in necessary elements
        mainScreen.blit(timerText, textRect)
        
        # Will draw/wipe the toggle "tooltip" as needed.
        if isDrawing: mainScreen.blit(hideToggleText, toggleRect)
        else: mainScreen.blit(toggleText, toggleRect)
        
        pygame.time.set_timer(DRAWING_TIME_COMPLETE, 60000)
        
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            
            # Detects a click (human double blink) and toggles the drawing mode. 
            if event.type == pygame.MOUSEBUTTONDOWN:
                isDrawing = not isDrawing

            if event.type == pygame.MOUSEMOTION and isDrawing:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(mainScreen, drawingColor, (pos[0], pos[1]), 5.0)
                
                        
        pygame.display.update()