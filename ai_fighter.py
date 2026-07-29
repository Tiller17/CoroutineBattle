import random
from fighter import Fighter


class AIFighter(Fighter):

    def take_turn(self, opponent):

        while self.is_alive():

            move = random.choice(self.moves)

            print(f"\n{self.name} chose {move.name}")


            self.attack_enemy(opponent, move)


            yield
