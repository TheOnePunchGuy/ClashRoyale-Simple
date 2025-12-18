import pygame
import time

from src.towers import Towers, enemy_ptower_left, enemy_ptower_right, player_ptower_left, player_ptower_right, enemy_crown_tower, player_crown_tower

start_time = pygame.time.get_ticks() // 1000  #convert to seconds

#make elixir
class Elixir():
    def __init__(self, card, e_cost, elixir_count):
        self.card = card
        self.e_cost = e_cost
        self.elixir_count = elixir_count

    def elix_interval(self):
        current_time = pygame.time.get_ticks() // 1000
        single_elix_interval = 2.8
        double_elix_interval = 1.4
        triple_elix_interval = 0.9
        elixir = single_elix_interval
        if current_time == 120: #after 2 minute
            elixir = double_elix_interval
        elif current_time == 240: #after 4 minutes
            elixir = triple_elix_interval
        return elixir

    def elixir_regen(self, elixir_count):
        elixir = self.elix_interval(Elixir)
        time_elapsed = pygame.time.get_ticks() // 1000  #convert to seconds
        if time_elapsed >= elixir:
            if self.elixir_count < 10: #max elixir count is 10
                self.elixir_count += 1
                time_elapsed = 0
                return self.elixir_count

    def subtract_elixir(self, card, e_cost, elixir_count):
        #if elixir count is less than card cost, cannot play card
        if card.e_cost > self.elixir_count:
            return False
        
        #if elixir count is greater than or equal to card cost, can play card
        elif card.e_cost <= self.elixir_count:
            return True
    
#attack
#path finding
#towers

class Gamelogic():
    def tower_down(self, current_time):
        #game lost conditions based on tower hp and time elapsed
        if player_ptower_left.hp <= 0 and enemy_ptower_left.hp > 0 and enemy_ptower_right.hp > 0:
            if current_time >= 180:  #after 3 minutes
                self.game_lost()
        elif player_ptower_right.hp <= 0 and enemy_ptower_right.hp > 0 and enemy_ptower_left.hp > 0:
            if current_time >= 180:  #after 3 minutes
                self.game_lost()

        #game won conditions based on tower hp and time elapsed
        elif enemy_ptower_right.hp <= 0 and player_ptower_right.hp > 0 and player_ptower_left.hp > 0:
            if current_time >= 180:  #after 3 minutes
                self.game_won()
        elif enemy_ptower_left.hp <= 0 and player_ptower_left.hp > 0 and player_ptower_right.hp > 0:
            if current_time >= 180:  #after 3 minutes
                self.game_won()

    def crown(self):
        if player_crown_tower.hp <= 0 and enemy_crown_tower.hp > 0:
            self.game_won()
        pass

    def game_won(self):
        pass

    def game_lost(self):
        pass

#clock
#crown
#win/loss
