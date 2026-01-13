import pygame
import time
import random

from src.towers import Towers, enemy_ptower_left, enemy_ptower_right, player_ptower_left, player_ptower_right, enemy_crown_tower, player_crown_tower

start_time = pygame.time.get_ticks() // 1000  #convert to seconds

#make elixir
class Elixir():
    def __init__(self, elixir_count):
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

    def elixir_regen(self):
        elixir = self.elix_interval()
        time_elapsed = pygame.time.get_ticks() // 1000  #convert to seconds
        if time_elapsed >= elixir:
            time_elapsed = 0
            if self.elixir_count < 10: #max elixir count is 10
                self.elixir_count += 1
                return self.elixir_count

    def can_subtract_elixir(self, card):
        #if elixir count is less than card cost, cannot play card
        if card.e_cost > self.elixir_count:
            return False
        
        #if elixir count is greater than or equal to card cost, can play card
        elif card.e_cost <= self.elixir_count:
            return True
        
    def subtract_elixir(self, card):
        if self.can_subtract_elixir(card):
            self.elixir_count -= card.e_cost
            return self.elixir_count
    

player_elixir = Elixir(1)

#attack
#path finding
#towers

class Gamelogic():
    def tower_down(self, current_time):
        enemy_crowns = 0
        player_crowns = 0
        
        if player_ptower_left.hp or player_ptower_right.hp <= 0:
            enemy_crowns += 1

        elif enemy_ptower_left or enemy_ptower_right <= 0:
            player_crowns += 1

        if current_time >= 180:
            if player_crowns > enemy_crowns:
                self.game_won()
            
            elif enemy_crowns > player_crowns:
                self.game_lost()
            
            else:
                self.game_tied()

        if player_crown_tower.hp <= 0:
            self.game_lost()

        if enemy_crown_tower.hp <= 0:
            self.game_won()

        print(player_crowns)
        
        '''
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
        '''

    def crown(self):
        if player_crown_tower.hp <= 0 and enemy_crown_tower.hp > 0:
            self.game_won()
        pass

    def game_won(self):
        pass

    def game_lost(self):
        pass

    def arena_change(self):
        pass

class Enemy():
    def enemy_spawn(self):
        pass
#clock
#crown
#win/loss
