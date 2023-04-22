import pygame
import os

pygame.init()
WIDTH = 500
HEIGHT = 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save your dream")  # title name

# 定义颜色 (Define colors)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60


#  图片素材库 Image Assets 
SCALE = (100, 100)  # 调整图片大小

PLAYER_IMAGE = pygame.image.load(os.path.join('game', 'player.gif'))
PLAYER = pygame.transform.scale(PLAYER_IMAGE, SCALE)

MS_WISE_IMAGE = pygame.image.load(os.path.join('game', 'wise.gif'))
MS_WISE = pygame.transform.scale(MS_WISE_IMAGE, SCALE)

APPLE_IMAGE = pygame.image.load(os.path.join('game', 'apple.gif'))
APPLE = pygame.transform.scale(APPLE_IMAGE, SCALE)

# set up the text surface
# text = font.render("Please enter your name:", True, (255, 255, 255))
# text_rect = text.get_rect(center=(320, 240))


# render some txt onto a surface

def draw_window():
    LEFT_BOTTOM = (100, 300)  # pygame draw from top left
    LEFT_TOP = (100, 100)

    WINDOW.fill(BLACK) # background color
    WINDOW.blit(PLAYER, LEFT_BOTTOM)  # blit() is drawing things on the screen
    WINDOW.blit(APPLE, LEFT_TOP)  # apple hanging in the tree
    pygame.display.update()


def render_text(text: str):
    font = pygame.font.SysFont(None, 23)
    text_surface = font.render(text, True, (1, 1, 1))
    return text_surface

    #text_surface = render_text("Hello, world!")
    # blit the text onto the screen
    #  blit() method is used to copy one surface onto another surface.
    #WINDOW.blit(text_surface, (100, 100))


# 定义对话及选项 (Define dialogues and options)
dialogue = {
    "start": {
        "text": "Welcome! Please choose an option.",
        "options": ["Option 1", "Option 2"],
        "branches": ["branch1", "branch2"],
    },
    "branch1": {
        "text": "You chose Option 1. The story continues...",
        "options": [],
        "branches": [],
    },
    "branch2": {
        "text": "You chose Option 2. The story continues...",
        "options": [],
        "branches": [],
    },
}

def main():
    # clock
    clock = pygame.time.Clock()
    # 主循环 (Main loop)
    run = True
    while run:
        clock.tick(FPS)  # never go over FPS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            pygame.display.update()
            draw_window()

    # last line of while loop
    pygame.quit()

if __name__ == "__main__":
    main()