from fighter import Fighter


class PlayerFighter(Fighter):

    def take_turn(self, opponent):

        while self.is_alive():

            print("\nChoose a move:")

            for i, move in enumerate(self.moves):
                print(f"{i + 1}. {move.name}")


            choice = int(input("> ")) - 1

            move = self.moves[choice]


            self.attack_enemy(opponent, move)


            yield
