import pygame, sys
import time

from button import Button
from drawing_canvas import drawingCanvasScreen
from utility_functions import get_font

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/images/darkBlueMountain.png")

def mainMenuScreen():
    while True:
        screen.blit(BG, (0, 0))

        menuMousePosition = pygame.mouse.get_pos()

        menuText = get_font(100).render("MAIN MENU", True, "#b68f40")
        menuRect = menuText.get_rect(center=(640, 100))

        playButton = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quitButton = Button(image=pygame.image.load("assets/images/QuitRect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menuText, menuRect)

        for button in [playButton, quitButton]:
            button.changeFontColor(menuMousePosition)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menuMousePosition):
                    playScreen()
                if quitButton.checkForInput(menuMousePosition):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def playScreen():
    while True:
        playMousePosition = pygame.mouse.get_pos()

        screen.fill("black")

        playScreenText = get_font(45).render("This is the PLAY screen.", True, "White")
        textRectangle = playScreenText.get_rect(center=(640, 160))
        screen.blit(playScreenText, textRectangle)

        # Defining the buttons drawn on the play screen.
        continueToCanvasButton = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 300), text_input="Draw!", font=get_font(75), base_color="White", hovering_color="Green")
        backButton = Button(image=pygame.image.load("assets/images/PlayRect.png"), pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")


        backButton.changeFontColor(playMousePosition)
        backButton.update(screen)
        continueToCanvasButton.changeFontColor(playMousePosition)
        continueToCanvasButton.update(screen)

        for event in pygame.event.get():
            # Handling any type of quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handling a click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if backButton.checkForInput(playMousePosition):
                    mainMenuScreen()
                if continueToCanvasButton.checkForInput(playMousePosition):
                    drawingCanvasScreen(screen)

        pygame.display.update()
        



if __name__ == "__main__":
    mainMenuScreen()