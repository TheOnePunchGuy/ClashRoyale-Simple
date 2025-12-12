class Troop:
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.range = range
        self.e_cost = e_cost
        self.range = range
        self.e_cost = e_cost
        self.special_ability = special_ability

    def pathfinding(self):
        pass

    def attack(self):
        pass

    def move(self):
        pass

    def use_ability(self):
        pass

    def die(self):
        pass

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()
#Regular troops
class Knight(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability)

class Archers(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability) 

class Skeletons(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability) 

#Swarm class
class Swarm(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability)

class Skeleton(Swarm):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability)

# Tank class (only target buildings/towers)
class Tank(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, range, e_cost, special_ability)

class Giant(Tank):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability)
    
# Special characters
class Dio(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability)

class Kira(Troop):
    def __init__(self, hp, speed, damage, range, e_cost, special_ability=False):
        super().__init__(hp, speed, damage, range, e_cost, special_ability)

# Buildings
class Buildings():
    def __init__(self, hp, damage, range, e_cost, ability=False):
        self.hp = hp
        self.damage = damage
        self.range = range
        self.ability = ability
        self.e_cost = e_cost
    
    def attack(self):
        pass
    def die(self):
        pass
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

class Cannon(Buildings):
    def __init__(self, hp, damage, range, e_cost, ability=False):
        super().__init__(hp, damage, range, ability, e_cost)

class Xbow(Buildings):
    def __init__(self, hp, damage, range, e_cost, ability=True):
        super().__init__(hp, damage, range, e_cost, ability)

#Spells
class Spells():
    def __init__(self, damage, area, speed, e_cost):
        self.damage = damage
        self.area = area
        self.speed = speed
        self.e_cost = e_cost
    def cast_spell(self):
        pass
    def spell_effect(self):
        pass
    def expire(self):
        pass

class Rocket(Spells):
    def __init__(self, damage, area, speed, e_cost):
        super().__init__(damage, area, speed, e_cost)

class Poison(Spells):
    def __init__(self, damage, area, speed, e_cost):
        super().__init__(damage, area, speed, e_cost)        

class Log(Spells):
    def __init__(self, damage, area, speed, e_cost):
        super().__init__(damage, area, speed, e_cost)