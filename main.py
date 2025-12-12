import pygame
pygame.init()

#file imports
import src.screen as screen
import src.arena as arena

#set up window
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Window")

#colour constants
GREEN = (0, 255, 0)
BROWN = (150, 75, 0)
PURPLE = (128, 0, 128)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        arena.draw_arena()
        screen.draw_deck()
        screen.draw_elixer()
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()

