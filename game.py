import pygame
import time
#make elixir
class Elixir:
    def __init__(self, card, e_cost, elixir_count):
        self.card = card
        self.e_cost = e_cost
        self.elixir_count = elixir_count
        
    def elixir_bar(self):
        #elixir generation over time
        single_elix_interval = 2.8
        double_elix_interval = 1.4
        triple_elix_interval = 0.9

        pass

    def subtract_elixir(self, card, e_cost, elixir_count):
        #if elixir count is less than card cost, cannot play card
        if card.e_count > self.elixir_count:
            return False
        
        #if elixir count is greater than or equal to card cost, can play card
        elif card.e_count <= self.elixir_count:
            return True
    
        
#card placement
def card_location(TILE_SIZE):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        grid_x = mouse_x / TILE_SIZE
        grid_y = mouse_y / TILE_SIZE
        return(grid_x, grid_y)
    
#attack
#path finding
#towers

class Gamelogic():

    def game_clock(self):
        pass

    def crown(self):
        pass

    def game_won(self):
        pass
  

#clock
#crown
#win/loss
