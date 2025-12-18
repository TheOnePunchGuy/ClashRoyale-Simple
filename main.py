import pygame
pygame.init()

#file imports
import src.screen as screen
import src.game as game

#set up window
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 650
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Window")

#colour constants
GREEN = (0, 255, 0)
BROWN = (150, 75, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
TILE_SIZE = 27

def card_location(TILE_SIZE):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            grid_x = mouse_x // TILE_SIZE
            grid_y = mouse_y // TILE_SIZE
            return(grid_x, grid_y)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        #game.Gamelogic.game_clock(current_time)
        screen.draw_arena()
        screen.draw_deck()
        screen.draw_elixir()
        screen.draw_timers()
        pygame.display.update()
    pygame.quit()
if __name__ == "__main__":
    main()

