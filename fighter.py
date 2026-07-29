import random


class Fighter:

    def __init__(self, name, hp, attack, defense, speed, moves):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves


    def take_damage(self, damage):
        self.hp -= damage

        if self.hp < 0:
            self.hp = 0


    def is_alive(self):
        return self.hp > 0


    def attack_enemy(self, enemy, move):

        damage = move.power + self.attack - enemy.defense

        damage += random.randint(-3, 3)


        if random.randint(1, 10) == 1:
            print("Critical Hit!")
            damage *= 2


        if damage < 1:
            damage = 1


        enemy.take_damage(damage)


        print(f"{self.name} used {move.name}!")
        print(f"{enemy.name} took {damage} damage!")


    def take_turn(self, opponent):
        pass
