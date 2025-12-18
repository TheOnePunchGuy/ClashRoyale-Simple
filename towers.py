
class Towers:
    def __init__(self, tower_type, hp, damage, range, attack_speed, location):
        self.tower_type = tower_type
        self.hp = hp
        self.damage = damage
        self.range = range
        self.attack_speed = attack_speed
        self.location = location
    
    def hit_point_check(self):
        return self.hp
    
    def attack(self, target, range, damage, attack_speed):
        #if target is in range, target hp decreases by damage
        if target_in_range(target, range):
            pass

    def target_in_range(self, target, range):
        pass
    
    def die(self):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

class Crown_Tower(Towers):
    def __init__(self, tower_type, hp, damage, range, attack_speed, location):
        super().__init__(tower_type, hp, damage, range, attack_speed, location)

#princess tower setup
enemy_ptower_left = Towers("Enemy_Tower", 1000, 50, 5, 1.5, (0, 0))
enemy_ptower_right = Towers("Player_Tower", 1000, 50, 5, 1.5, (17, 23))
player_ptower_left = Towers("Player_Tower", 1000, 50, 5, 1.5, (17, 0))
player_ptower_right = Towers("Player_Tower", 1000, 50, 5, 1.5, (0, 23))
#crown tower setup
enemy_crown_tower = Crown_Tower("Enemy_Crown_Tower", 1500, 75, 7, 1.2, (0, 11))
player_crown_tower = Crown_Tower("Player_Crown_Tower", 1500, 75, 7, 1.2, (17, 11))