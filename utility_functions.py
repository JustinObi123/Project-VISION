import pygame
from pygame.locals import *

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/Roboto-Light.ttf", size)

def displayText(textToDisplay, position, mainScreen, backgroundScreen, fontSize=40):
    
    textSurface = get_font(fontSize).render(textToDisplay, True, "Black")
    textRect = textSurface.get_rect(topleft=position)
    
    mainScreen.blit(backgroundScreen.subsurface(textRect), position)
    mainScreen.blit(textSurface, position)
    pygame.display.update(textRect)
    return textRect