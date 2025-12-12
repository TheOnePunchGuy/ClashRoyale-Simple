import pygame
from src.arena import arena_map, TILE_SIZE, draw_arena
from main import WINDOW_HEIGHT, WINDOW_WIDTH, BROWN, PURPLE, WINDOW
#Set up arena dimensions and position
ARENA_WIDTH = TILE_SIZE * 18
ARENA_HEIGHT = TILE_SIZE * 24
ARENA_CORNER = (WINDOW_WIDTH // 2) - (ARENA_WIDTH // 2)
#Set up deck on screen
def draw_deck():
    pygame.draw.rect(WINDOW, PURPLE, (ARENA_CORNER, WINDOW_HEIGHT, 0, 0))
#Set up arena on screen

#Set up elixer on screen
def draw_elixer():
    pygame.draw.rect(WINDOW, PURPLE, (ARENA_CORNER, WINDOW_HEIGHT, ARENA_WIDTH, 0))