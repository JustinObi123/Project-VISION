# import sys
# import pygame
# from pygame.locals import *

# from utility_functions import get_font, displayText
# from button import Button

# DOUBLE_CLICK_TIME = 1
# CANVAS_BACKGROUND_COLOR = "White"
# TICK_TIMER = pygame.USEREVENT + 1


# def drawingCanvasScreen(mainScreen):
#     mousePosition = pygame.mouse.get_pos()
#     timeRemaining = 60
#     isDrawing = False
#     drawingColor = (0, 0, 0)
#     timer = pygame.time.Clock()
    
#     mainScreen.fill(CANVAS_BACKGROUND_COLOR)
#     drawingSurface = pygame.Surface(mainScreen.get_size())
#     drawingSurface.fill(CANVAS_BACKGROUND_COLOR)
#     pygame.time.set_timer(TICK_TIMER, 1000)
    
#     while True:
#         # Progress the internal clock to tick game timer.
#         timer.tick(60)
        
#         # Declare a background surface to separate the drawing layer from the text layer.
#         displayText(f"Time Remaining: {timeRemaining}", (80, 20), fontSize=20, mainScreen=mainScreen, backgroundScreen=drawingSurface)
#         displayText(f"Blink twice to toggle!", (620, 30), mainScreen=mainScreen, backgroundScreen=drawingSurface)
    
#         # clearButtonPosition = (10, 700)
#         clearButton = Button(image=None, pos=(1080, 650), text_input="Clear", font=get_font(30), base_color="Black", hovering_color="Green")
#         pygame.draw.rect(drawingSurface, "Red", clearButton.rect)
        
#         for button in [clearButton]:
#             button.update(mainScreen)
        
#         # Event loop.
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()   
#                 sys.exit()
            
#             # Detects a click (human double blink) and toggles the drawing mode. 
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 isDrawing = not isDrawing
#                 if not isDrawing:
#                     if clearButton.checkForInput(mousePosition):
#                         mainScreen.fill("White")
#                         takeScreenshot(drawingSurface)
                    
                    

#             # Plots a circle if the mouse is in mortion and drawing mode is active.
#             if event.type == pygame.MOUSEMOTION and isDrawing:
#                 pos = pygame.mouse.get_pos()
#                 pygame.draw.circle(mainScreen, drawingColor, (pos[0], pos[1]), 5.0)
                
#             # Handling TICK_TIMER event here.
#             if event.type == TICK_TIMER: 
#                 if timeRemaining <= 0:
#                     pygame.time.set_timer(TICK_TIMER, 0)
#                     pass # TODO: Call the next screen here.
#                 else:
#                     timeRemaining -= 1
            
                
                        
#         pygame.display.update()


# def takeScreenshot(screenshotLayer, filename="userDrawing.jpg"): pygame.image.save(screenshotLayer, filename)
import sys
import pygame
from pygame.locals import *

# from scenario import scenarioScreen
from utility_functions import get_font, displayText
from button import Button

DOUBLE_CLICK_TIME = 1
CANVAS_BACKGROUND_COLOR = "White"
TICK_TIMER = pygame.USEREVENT + 1
def drawingCanvasScreen(mainScreen):
    timeRemaining = 60
    isDrawing = False
    drawingColor = (0, 0, 0)
    timer = pygame.time.Clock()
    
    mainScreen.fill(CANVAS_BACKGROUND_COLOR)
    drawingSurface = pygame.Surface(mainScreen.get_size())
    drawingSurface.fill(CANVAS_BACKGROUND_COLOR)
    pygame.time.set_timer(TICK_TIMER, 1000)
    
    # Initialize the clear button once, outside the main loop
    clearButton = Button(
        image=None,
        pos=(1080, 650),
        text_input="Finish",
        font=get_font(30),
        base_color="Black",
        hovering_color="Green"
    )
    
    while True:
        # Progress the internal clock to tick game timer.
        timer.tick(60)
        
        # Declare a background surface to separate the drawing layer from the text layer.
        displayText(
            f"Time Remaining: {timeRemaining}",
            (80, 20),
            fontSize=20,
            mainScreen=mainScreen,
            backgroundScreen=drawingSurface
        )
        displayText(
            f"Blink twice to toggle!",
            (620, 30),
            mainScreen=mainScreen,
            backgroundScreen=drawingSurface
        )
    
        # Draw the clear button on the main screen
        pygame.draw.rect(mainScreen, "#84a65b", clearButton.rect)
        clearButton.update(mainScreen)
        
        # Event loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                sys.exit()
            
            # Detects a click (human double blink) and toggles the drawing mode. 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # Get the current mouse position
                
                if not isDrawing and clearButton.checkForInput(mouse_pos):
                    # If not in drawing mode and the clear button is clicked
                    takeScreenshot(mainScreen)
                    pygame.time.set_timer(TICK_TIMER, 0)
                    scenarioScreen(mainScreen, "rot2.")
                else:
                    # Toggle drawing mode
                    isDrawing = not isDrawing
                
            # Plots a circle if the mouse is in motion and drawing mode is active.
            if event.type == pygame.MOUSEMOTION and isDrawing:
                pos = pygame.mouse.get_pos()
                pygame.draw.circle(mainScreen, drawingColor, pos, 5)
                
            # Handling TICK_TIMER event here.
            if event.type == TICK_TIMER: 
                if timeRemaining <= 0:
                    takeScreenshot(mainScreen)
                    pygame.time.set_timer(TICK_TIMER, 0)
                    scenarioScreen(mainScreen, "rot2.")
                else:
                    timeRemaining -= 1
                    
        pygame.display.update()
def takeScreenshot(screenshotLayer, filename="assets/images/userDrawing.jpg"): 
    pygame.image.save(screenshotLayer, filename)

# pygame.init()

# Define a consistent color scheme
COLOR_SCHEME = {
    "background": (30, 30, 30),        # Dark Gray
    "primary": (0, 76, 100),           # Teal
    "accent": (183, 143, 64),          # Gold
    "text": (255, 255, 255),           # White
    "button_base": (215, 252, 212),    # Light Green
    "button_hover": (255, 255, 255),   # White
}

# Set up screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
# mainScreen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scenario Screen")



def wrap_text(text, font, max_width):
    """
    Wraps text to fit within a given width when rendered.
    """
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        line_width, _ = font.size(test_line)

        if line_width <= max_width:
            current_line = test_line
        else:
            if current_line:  # Avoid adding empty lines
                lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())
    return lines

def get_fitting_font(text, font_name, area_rect, max_font_size=100, min_font_size=10):
    """
    Finds the largest font size that allows the text to fit within the specified area.
    """
    font_size = max_font_size
    while font_size >= min_font_size:
        font = pygame.font.Font(font_name, font_size)
        wrapped_lines = wrap_text(text, font, area_rect.width)
        line_height = font.get_linesize()
        total_height = line_height * len(wrapped_lines)
        if total_height <= area_rect.height:
            return font
        font_size -= 1
    return pygame.font.Font(font_name, min_font_size)  # Fallback to minimum font size

def scenarioScreen(mainScreen, scenarioInput):
    """
    Displays the scenario screen with wrapped text and a next button.
    """
    clock = pygame.time.Clock()  # Initialize clock for frame rate control

    # Define text area with padding
    padding = 50
    text_area = pygame.Rect(padding, 170, SCREEN_WIDTH - 2 * padding, 390)
    text = scenarioInput

    # Choose a font that fits the text area
    font_path = None  # Use default font
    font = get_fitting_font(text, font_path, text_area)

    # Create the next button before the loop
    nextButton = Button(
        image=pygame.image.load("assets/images/PlayRect.png").convert_alpha(),
        pos=(SCREEN_WIDTH // 2, 630),
        text_input="DRAW",
        font=get_font(75),
        base_color=COLOR_SCHEME["button_base"],
        hovering_color=COLOR_SCHEME["button_hover"]
    )

    running = True
    while running:
        clock.tick(60)  # Limit to 60 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                scenarioMousePosition = pygame.mouse.get_pos()
                if nextButton.checkForInput(scenarioMousePosition):
                    drawingCanvasScreen(mainScreen)  # Make sure this function is defined

        # Get mouse position
        scenarioMousePosition = pygame.mouse.get_pos()

        # Fill background
        mainScreen.fill(COLOR_SCHEME["background"])

        # **Removed the rectangle around the scenario text**
        # Previously, a rectangle was drawn here to highlight the text area.
        # Since the user requested its removal, the corresponding line is deleted.

        # Wrap and render text
        wrapped_lines = wrap_text(text, font, text_area.width)
        y_offset = text_area.top

        for line in wrapped_lines:
            text_surface = font.render(line, True, COLOR_SCHEME["text"])
            mainScreen.blit(text_surface, (text_area.left, y_offset))
            y_offset += font.get_linesize()
            if y_offset > text_area.bottom:
                break  # Stop drawing if exceeding the text area

        # Render "Scenario" title
        title_font = get_font(100)
        scenarioText = title_font.render("Scenario", True, COLOR_SCHEME["accent"])
        scenarioRect = scenarioText.get_rect(center=(SCREEN_WIDTH // 2, 70))  # Centered horizontally
        mainScreen.blit(scenarioText, scenarioRect)

        # Update and render the next button
        nextButton.changeFontColor(scenarioMousePosition)
        nextButton.update(mainScreen)

        pygame.display.update()