
start_game =0
def game_rock():

    while True:
        player1_input = input("Please select one option : > ")
        player2_input = input("Please select one option : > ")
        if player1_input == "Rock":
            if player2_input=="Scissor":
                print("Player 1 is winner")
            elif player2_input== "Paper":
                print("Player 2 wins")
            else:
                print("Tie")

        elif player1_input == "Scissor":
            if player2_input == "Paper":
                print("Player 1 wins")
            elif player2_input == "Rock":
                print("Player 2 wins")
            else:
                print("Tie")

        elif player1_input == "Paper":
            if player2_input == "Scissor":
                print("Player 1 wins")
            elif player2_input == "Rock":
                print("Player 2 wins")
            else:
                print("Tie")

        else:
           print("invalid input")

        a =input("Please enter 0 or 1 : 0 if you wish to replay else 1 > ")
        if a=="1":
            break





print(game_rock())
















