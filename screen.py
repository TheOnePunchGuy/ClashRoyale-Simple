import pygame
from src.arena import arena_map, arena_map
from main import WINDOW, WINDOW_HEIGHT, WINDOW_WIDTH, GREEN, PURPLE, BLACK, GREY, BLUE, WHITE, TILE_SIZE
from src.game import Elixir
#Set up arena dimensions and position
ARENA_WIDTH = TILE_SIZE * 18
ARENA_HEIGHT = TILE_SIZE * 24

#Set up arena on screen
def draw_arena():
    for r in range(len(arena_map)):
        for c in range(len(arena_map[r])):
            for l in range(len(arena_map[r][c])):
                tile = arena_map[r][c][l]
                
                if tile == 0:
                    pygame.draw.rect(WINDOW, GREEN, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65))
                    pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65), 1)
                
                elif tile == 1:
                    pygame.draw.rect(WINDOW, BLUE, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65))
                    pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65), 1)
                
                elif tile == 2:
                    pygame.draw.rect(WINDOW, GREY, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65))
                    pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65), 1)
                
                elif tile == 3:
                    pygame.draw.rect(WINDOW, WHITE, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65))
                    pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE * 0.65, TILE_SIZE, TILE_SIZE * 0.65), 1)

#Set up elixer on screen
def draw_elixir():
    current_elixir = 0
    elixir_count = Elixir.elixir_regen(Elixir, current_elixir)
    for i in range(elixir_count):
        pygame.draw.rect(WINDOW, PURPLE, (ARENA_WIDTH + 10 + (i * 20), WINDOW_HEIGHT - 30, 15, 25))
        pass
    

#Set up deck on screen
def draw_deck():
    pygame.draw.rect(WINDOW, GREY, (ARENA_WIDTH, 0, 108, WINDOW_HEIGHT))

#Set up timers on screen
def draw_timers():
    pygame.draw.rect(WINDOW, BLACK, (ARENA_WIDTH, 0, WINDOW_WIDTH, 108))