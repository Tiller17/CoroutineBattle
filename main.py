from move import Move
from player_fighter import PlayerFighter
from ai_fighter import AIFighter
from battle import battle


def main():

    slash = Move("Slash", 15)
    fireball = Move("Fireball", 20)
    heavy = Move("Heavy Strike", 25)
    quick = Move("Quick Attack", 10)


    player = PlayerFighter(
        "Hero",
        100,
        12,
        6,
        10,
        [slash, fireball, heavy, quick]
    )


    enemy = AIFighter(
        "Goblin",
        100,
        10,
        5,
        8,
        [slash, heavy, quick]
    )


    print("===================")
    print(" Coroutine Battle ")
    print("===================")


    battle(player, enemy)



if __name__ == "__main__":
    main()
