import sys
import pygame
from pygame.locals import *

from time import sleep

# TODO: Complete scenario screen!!!
def scenarioScreen(mainScreen):
    mainScreen.fill("Black")
    
   # Main code for drawing elements goes here. 
    while True:
        sleep(1)
        pass
        
        # Event loop. Any events built-in or modified by you go here.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    sys.exit()
                    
                    
    