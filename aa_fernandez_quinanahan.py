class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        zombie.take_damage(self.damage)

    def take_damage(self, zombie_damage):
        self.health -= zombie_damage


class zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        if self.distance > 0:
            self.distance-=1

    def attack_plant(self, plant): 
        plant.take_damage(self.damage)

    def take_damage(self, plant_damage):
        self.health -= plant_damage

def main():
    Bonkchoy = Plant("Bonk choy", 150, 50)
    Peashooter = Plant("Peashooter", 100, 75)
    Buckethead = zombie("Bucket Head", 500, 75)

    turn = 1

    while True:
        print("Turn", turn)
        print("Zombie health", zombie.health)
        print("Zombie distance", zombie.distance)
        print("Bonkchoy health", Bonkchoy.health)
        print("Peashooter health", Peashooter.health)
        