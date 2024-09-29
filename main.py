import pygame, sys
import time

from button import Button

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/images/darkBlueMountain.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/fonts/Roboto-Light.ttf", size)

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
            button.changeColor(menuMousePosition)
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


        backButton.changeColor(playMousePosition)
        backButton.update(screen)
        continueToCanvasButton.changeColor(playMousePosition)
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
                    drawingCanvasScreen()

        pygame.display.update()
        
    
# TODO: Complete scenario screen!!!
# def scenarioScreen():
#     playMousePosition = pygame.mouse.get_pos()

#     screen.fill("black")

#     playScreenText = get_font(25).render("Here is your scenario:", True, "White")
#     textRectangle = playScreenText.get_rect(center=(640, 260))
#     screen.blit(playScreenText, textRectangle)
    
DOUBLE_CLICK_TIME = 1
CANVAS_BACKGROUND_COLOR = "White"
def drawingCanvasScreen():
    # playMousePosition = pygame.mouse.get_pos()
    timeRemaining = 60
    isDrawing = False
    drawingColor = (0, 0, 0)
    
    screen.fill(CANVAS_BACKGROUND_COLOR)
    
    while True:
        
        # Declaring text elements
        timerText = get_font(20).render(f"Time Remaining: {timeRemaining}", True, "Black")
        toggleText = get_font(40).render("Blink twice to toggle!", True, "Black")
        hideToggleText = get_font(40).render("Blink twice to toggle!", True, CANVAS_BACKGROUND_COLOR)
        
        
        # Declaring text bounding boxes
        textRect = timerText.get_rect(center=(100, 20))
        toggleRect = toggleText.get_rect(center=(640, 30)) # Same bounding box can be used for the toggle text and hide toggle text.
        
        # Blitting in necessary elements
        screen.blit(timerText, textRect)
        
        # Will draw/wipe the toggle "tooltip" as needed.
        if isDrawing: screen.blit(hideToggleText, toggleRect)
        else: screen.blit(toggleText, toggleRect)
        
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            
            #    
            if event.type == pygame.MOUSEBUTTONDOWN:
                isDrawing = not isDrawing

            if event.type == pygame.MOUSEMOTION and isDrawing:
                pos =  pygame.mouse.get_pos()
                pygame.draw.circle(screen, drawingColor, (pos[0], pos[1]), 5.0)
                
                        
        pygame.display.update()



if __name__ == "__main__":
    mainMenuScreen()