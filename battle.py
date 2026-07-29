def battle(player, enemy):

    player_turn = player.take_turn(enemy)

    enemy_turn = enemy.take_turn(player)


    while player.is_alive() and enemy.is_alive():

        print("\n------------------")
        print(f"{player.name}: {player.hp} HP")
        print(f"{enemy.name}: {enemy.hp} HP")
        print("------------------")


        if player.speed >= enemy.speed:

            if player.is_alive():
                next(player_turn)


            if enemy.is_alive():
                next(enemy_turn)


        else:

            if enemy.is_alive():
                next(enemy_turn)


            if player.is_alive():
                next(player_turn)



    print("\n===================")


    if player.is_alive():
        print("You Win!")

    else:
        print("You Lose!")
