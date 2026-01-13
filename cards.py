import os
import pygame
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from src.arena import arena_map
import src.animation as animation
import pyganim

TILE_SIZE = 27

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "pictures")
ANI_DIR_KNIGHT = os.path.join(BASE_DIR, 'cardknight')
ANI_DIR_TOWER_R = os.path.join(BASE_DIR, 'towers')
DIR_MENU_LOADING = os.path.join(IMG_DIR, "Loading.jpg")
DIR_MENU_LOGO = os.path.join(IMG_DIR, "Logo.jpg")


class Troop:
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.range = range
        self.attack_range = attack_range
        self.attack_cooldown = attack_cooldown
        self.e_cost = e_cost
        self.x = x
        self.y = y
        self.pos = pygame.Vector2(self.x, self.y)
        self.card_png = card_png
        self.card_animation = card_animation
        self.is_friendly = is_friendly
        self.special_ability = special_ability

    def pathfinding(self, start_x, start_y, end_x, end_y):
        grid = Grid(matrix=arena_map)
        start = grid.node(start_x, start_y)
        end = grid.node(end_x, end_y)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
        path = finder.find_path(start, end, grid)[0]
        return path
        
    def attack_radius(self, placed_card):
        radius = self.character_rect().inflate(self.range, self.range)
        for enemy in placed_card:
            if enemy.is_friendly != self.is_friendly:
                if radius.colliderect(enemy.character_rect()):
                    return enemy 
        return None

    def attack(self, placed_card, now_attack):
        attack_range = self.character_rect().inflate(self.attack_range, self.attack_range)
        enemy = self.attack_radius(placed_card)
        if enemy:
            self.x, self.y = self.move(self.x, self.y, int(enemy.x) // TILE_SIZE, int(enemy.y) // TILE_SIZE)
            self.pos = pygame.Vector2(enemy.x - self.x, enemy.y - self.y)
            if attack_range.colliderect(enemy.character_rect()):
                print(now_attack)
                if now_attack:
                    enemy.take_damage(self.damage, enemy)
                    now_attack = False
                else:
                    enemy.take_damage(0, enemy)
                return True
        return False


    def move(self, pos_x, pos_y, dest_x, dest_y):

        path = self.pathfinding(int(pos_x // TILE_SIZE), int(pos_y // TILE_SIZE), dest_x, dest_y)
        

        if len(path) <= 1:
            return pos_x, pos_y
        
        endpos_x, endpos_y = path[1]
        
        target_x = endpos_x * TILE_SIZE
        target_y = endpos_y * TILE_SIZE

        
        if pos_x < target_x:
            pos_x += self.speed
           
            if pos_x > target_x: 
                pos_x = target_x

        elif pos_x > target_x:
            pos_x -= self.speed
            if pos_x < target_x: 
                pos_x = target_x

        if pos_y < target_y:
            pos_y += self.speed
            if pos_y > target_y: 
                pos_y = target_y

        elif pos_y > target_y:
            pos_y -= self.speed
            if pos_y < target_y: 
                pos_y = target_y

        self.pos = pygame.Vector2(dest_x - pos_x, dest_y - pos_y)

        return pos_x, pos_y

    def use_ability(self):
        pass

    def die(self, card):
        placed_card.remove(card)
        

    def take_damage(self, damage, card):
        self.hp -= damage
        if self.hp <= 0:
            self.die(card)

    def image_pathing(self):
        image = pygame.image.load(self.card_png).convert_alpha()
        scaled_image = pygame.transform.scale(image, (108, 142))
        return scaled_image
    
    def get_direction(self):
        angle = self.pos.as_polar()[1]
        if 45 <= angle < 135:
            return 'N'
        elif 135 <= angle < 225:
            return 'W'
        elif 225 <= angle < 315:
            return 'S'
        else:
            return 'E'

    def animation(self, card):
        direction = self.get_direction()
        
        if isinstance(card, Knight):
            card_ani = card_animation_list[0]
        elif isinstance(card, The_Guy):
            card_ani = card_animation_list[1]

        if direction == 'E':
            
            return card_ani[1]
        elif direction == 'N':
            
            return card_ani[2]
        elif direction == 'S':
            
            return card_ani[3]
        elif direction == 'W':
            return card_ani[1]  
        

    def character_rect(self):
        character_rect = self.animation(self).getCurrentFrame().get_rect(topleft=(self.x, self.y))
        return character_rect



#Regular troops
class Knight(Troop):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)

class Archers(Troop):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)

class Skeleton(Troop):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)

# Tank class (only target buildings/towers)
class Tank(Troop):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)
class Giant(Tank):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)
class The_Guy(Tank):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)
# Special characters
class Dio(Troop):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)
class Kira(Troop):
    def __init__(self, hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability=False):
        super().__init__(hp, speed, damage, range, attack_range, attack_cooldown, e_cost, x, y, card_png, card_animation, is_friendly, special_ability)
# Buildings
class Buildings():
    def __init__(self, hp, damage, range, e_cost, card_png, ability=False):
        self.hp = hp
        self.damage = damage
        self.range = range
        self.e_cost = e_cost
        self.card_png = card_png
        self.ability = ability
        
    
    def attack(self):
        pass

    def die(self):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

class Cannon(Buildings):
    def __init__(self, hp, damage, range, e_cost, card_png, ability=False):
        super().__init__(hp, damage, range, e_cost, card_png, ability)

class Xbow(Buildings):
    def __init__(self, hp, damage, range, e_cost, card_png, ability=True):
        super().__init__(hp, damage, range, e_cost, card_png, ability)

#Spells
class Spells():
    def __init__(self, damage, area, speed, e_cost, card_png):
        self.damage = damage
        self.area = area
        self.speed = speed
        self.e_cost = e_cost
        self.card_png = card_png
    
    def cast_spell(self):
        pass
    def spell_effect(self):
        pass
    def expire(self):
        pass

class Rocket(Spells):
    def __init__(self, damage, area, speed, e_cost, card_png):
        super().__init__(damage, area, speed, e_cost, card_png)
      

class Log(Spells):
    def __init__(self, damage, area, speed, e_cost, card_png):
        super().__init__(damage, area, speed, e_cost, card_png)

class Towers:
    def __init__(self, tower_type, hp, damage, range, attack_range, attack_cooldown, x, y, tower_animation, is_friendly):
        self.tower_type = tower_type
        self.hp = hp
        self.damage = damage
        self.range = range
        self.attack_range = attack_range
        self.attack_cooldown = attack_cooldown
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.tower_animation = tower_animation
        self.is_friendly = is_friendly
    
    def hit_point_check(self):
        return self.hp
    
    #for testing
    def attack_radius(self, placed_card):
        radius = self.character_rect().inflate(self.range, self.range)
        for enemy in placed_card:
            if enemy.is_friendly != self.is_friendly:
                if radius.colliderect(enemy.character_rect()):
                    return enemy 
        return None

    def attack(self, placed_card, now_attack):
        attack_range = self.character_rect().inflate(self.attack_range, self.attack_range)
        enemy = self.attack_radius(placed_card)
        if enemy:
            if attack_range.colliderect(enemy.character_rect()):
                if now_attack:
                    enemy.take_damage(self.damage, enemy)
                else:
                    enemy.take_damage(0, enemy)
                    
                return True
        return False
    
    def die(self, card):
        placed_card.remove(card)

    def take_damage(self, damage, card):
        self.hp -= damage
        if self.hp <= 0:
            self.die(card)
    
    def animation(self):
        image = pygame.image.load(self.tower_animation).convert_alpha()
        scaled_image = pygame.transform.scale(image, (10, 14))
        return scaled_image
    
    def character_rect(self):
        character_rect = self.animation().get_rect(topleft=(self.x, self.y))
        return character_rect

class Crown_Tower(Towers):
    def __init__(self, tower_type, hp, damage, range, attack_range, attack_cooldown, x, y, tower_animation, is_friendly):
        super().__init__(tower_type, hp, damage, range, attack_range, attack_cooldown, x, y, tower_animation, is_friendly)

#princess tower setup
enemy_ptower_left = Towers("Enemy_Tower", 1000, 50, 500, 5, 1.5, 1, 0, 0, False)
enemy_ptower_right = Towers("Player_Tower", 1000, 50, 500, 500, 1.5, 15, 5, os.path.join(ANI_DIR_TOWER_R, "tower.jpg"), False)
player_ptower_left = Towers("Player_Tower", 1000, 50, 5, 5, 1.5, 17, 0, 0, True)
player_ptower_right = Towers("Player_Tower", 1000, 50, 5, 5, 1.5, 0, 23, 0, True)
#crown tower setup
enemy_crown_tower = Crown_Tower("Enemy_Crown_Tower", 1500, 75, 7, 5, 1, 1.2, 11, 0, False)
player_crown_tower = Crown_Tower("Player_Crown_Tower", 1500, 75, 7, 5, 1.2, 17, 11, 0, False)


knight = Knight(1000, 1, 100, 500, 500, 1, 3, 0, 0, os.path.join(IMG_DIR, "knight.png"), None, False)
archers = Archers(10, 1, 1, 1, 1, 1, 0, 0, 0, os.path.join(IMG_DIR, "Archers.png"), None, False)
giant = Giant(10, 1, 1, 1, 1, 0, 1, 0, 0, os.path.join(IMG_DIR, "Giant.png"), None, False)
the_guy = The_Guy(10, 1, 1, 1, 1, 1, 0, 0, 0, os.path.join(IMG_DIR, "Golem.png"), None, False)
#skeletons = Skeleton(10, 1, 1, 1, 1, 1, 0, 0, 0, (0, 0), os.path.join(IMG_DIR, "Archers.png"), None, False)
#skeleton_army = Skeletons(10, 1, 1, 1, 1, 1, 0, 0, 0, (0, 0),os.path.join(IMG_DIR, "Archers.png"), None, False)
#dio = Dio(10, 1, 1, 1, 1, 1, 0, 0, 0, (0,0), os.path.join(IMG_DIR, "Archers.png"), None, False)
#kira = Kira(10, 1, 1, 1, 1, 1, 0, 0, 0, (0,0), os.path.join(IMG_DIR, "Archers.png"), None, False)
#cannon = Cannon(10, 1, 1, 1, 1, 1, 0, 0, 0, (0,0), os.path.join(IMG_DIR, "Archers.png"), None, False)
#xbow = Xbow(10, 1, 1, 1, 1, 1, 0, 0, 0, (0,0), os.path.join(IMG_DIR, "Archers.png"), None, False)
#rocket = Rocket(10, 1, 1, 1, 1, 1, 0, 0, 0, (0,0),os.path.join(IMG_DIR, "Archers.png"), None, False)
#log = Log(10, 1, 1, 1, 1, 1, 0, 0, 0, (0,0), os.path.join(IMG_DIR, "Archers.png"), None, False)


deck = [knight, archers, giant, the_guy]
placed_card = []
enemy_card = []

card_animation_list = [
    (knight, animation.knight_walk_E, animation.knight_walk_N, animation.knight_walk_S),
    (the_guy, animation.golem_walk_E, animation.golem_walk_N, animation.golem_walk_S),
]

#makes sure that the decks are consistent
def decks():
    pass
