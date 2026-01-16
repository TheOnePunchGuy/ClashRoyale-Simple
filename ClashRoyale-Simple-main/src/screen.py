import pygame
from src.arena import arena_map
from main import WINDOW, WINDOW_HEIGHT, WINDOW_WIDTH, GREEN, PURPLE, BLACK, GREY, BLUE, WHITE, TILE_SIZE
import src.game as game
from src.cards import deck, Towers, Crown_Tower
import src.animation as animation
import pyganim
#Set up arena dimensions and position
ARENA_WIDTH = TILE_SIZE * 18
ARENA_HEIGHT = TILE_SIZE * 24



#Set up arena on screen
def draw_arena():
    for r in range(len(arena_map)):
        for c in range(len(arena_map[r])):
            tile = arena_map[r][c]

            if tile == 0:
                pygame.draw.rect(WINDOW, BLUE, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

            elif tile == 1:
                pygame.draw.rect(WINDOW, GREEN, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

            else:
                pygame.draw.rect(WINDOW, GREY, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                pygame.draw.rect(WINDOW, BLACK, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

#Set up elixir on screen

def draw_elixir():
    for i in range(game.player_elixir.elixir_count):
        pygame.draw.rect(WINDOW, PURPLE, (WINDOW_WIDTH - 10, WINDOW_HEIGHT - (i * 20), 15, 155))
        
#Set up deck on screen
def draw_deck():
    WINDOW.blit(deck[0]().image_pathing(), (ARENA_WIDTH, 0))
    global rect_1
    rect_1 = deck[0]().image_pathing().get_rect(topleft=(ARENA_WIDTH, 0))

    WINDOW.blit(deck[1]().image_pathing(), (ARENA_WIDTH, 142))
    global rect_2
    rect_2 = deck[1]().image_pathing().get_rect(topleft=(ARENA_WIDTH, 0))
    
    WINDOW.blit(deck[2]().image_pathing(), (ARENA_WIDTH, 284))
    global rect_3
    rect_3 = deck[2]().image_pathing().get_rect(topleft=(ARENA_WIDTH, 0))

    WINDOW.blit(deck[3]().image_pathing(), (ARENA_WIDTH, 426))
    global rect_4
    rect_4 = deck[3]().image_pathing().get_rect(topleft=(ARENA_WIDTH, 0))

def draw_cards(selected_card, grid_x, grid_y):
    card_ani = selected_card.animation(selected_card)
    card_ani.blit(WINDOW, (grid_x, grid_y))
    
def draw_towers(tower_list):
    for tower in tower_list:
        tower_picture = tower.animation()
        WINDOW.blit(tower_picture, (tower.x, tower.y))
        
'''
def draw_timers():
    pygame.draw.rect(WINDOW, BLACK, (ARENA_WIDTH, 0, WINDOW_WIDTH, 108))
'''