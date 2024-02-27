print("\nWelcome to Treasure Island. Your mission is to find the treasure.")
print("You will be given options during your adventure, can you ")
print("find the treasure or will you be met with an untimely demise?\n")

game_over = False

while not game_over:
    cross_road_input = input("You're at a cross road that forks in two directions, where do you want to go? (Left or Right):\n ").lower()
    if cross_road_input == "right":
        print("You fall through a booby trapped path and are trapped forever next to other bold adventurers, Game Over!")
        game_over = True
        break

    lake_input = input("You come to a lake. THere is an island in the middle of the lake. Do you want to wait for a boat or swim across? (Wait or Swim): \n").lower()
    if lake_input == "swim":
        print("You are eaten by sharks, Game Over!")
        game_over = True
        break

    house_door_input = input("You arrive at the island unharmed. There is a hourse with 3 doors - red, yellow, and blue. Which color door do you choose to enter? (Red, Yellow, or Blue): \n").lower()
    if house_door_input == "blue":
        print("You enter a room full of man-eating birds, Game Over!")
        game_over = True
        break
    elif house_door_input == "yellow":
        print("Ahoy, you have found the treaure!")
        game_over = True
        break
    elif house_door_input == "red":
        print("You enter a dark room and the door locks behind you. The room is cursed and you are banished to the underworld, Game Over!")
        game_over = True
        break

