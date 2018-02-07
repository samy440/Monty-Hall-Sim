import sys, multiplayer_generator

def main():
    print("""\n\n\n\tWelcome to this Monty Hall Problem Simulator!\n
\tThis program aims to run simulations of the Monty Hall Problem
\twith the stay/switch strategiesand plot their outcome in 
\treal time.\n""")
    input_number_of_iterations = input("\n\tPlease input the number of simulations to run (or q to quit):  ")
    valid_input_n = intInput(input_number_of_iterations)
    while (valid_input_n < 1):
        print("\n\tThe input value for the number of simulations to run must be an integer.")
        print("\n\tYou have entered a " + str(type(input_number_of_iterations)) + " of value " + str(valid_input_n) + ".\n")
        input_number_of_iterations = input("\n\tPlease input the number of simulations to run (or q to quit):  ")
        valid_input_n = intInput(input_number_of_iterations)
    input_number_of_players = input("\n\n\n\tThanks! Now please input the number of independent players (between 1 and 9, including each endpoint) you want to have in each sim. (or q to quit):  ")
    valid_input_p = intInput(input_number_of_players)
    while ((valid_input_p < 1) or (valid_input_p > 9)) :
        print("\n\tThe input value for the number of players to have in each simulation must be an integer between 1 and 9.")
        print("\n\tYou have entered a " + str(type(input_number_of_players)) + " of value " + str(valid_input_p) + ".\n")
        input_number_of_players = input("\n\tPlease input the number of independent players (between 1 and 9) you want to have in each sim (or q to quit):  ")
        valid_input_p = intInput(input_number_of_players)
    print("\n\n\n\tThank you! Now please input an integer (between 0 and 100, including the endpoints) representing how likely it is for each player to decide to switch doors. ")
    list_of_player_switch_probabilities = []
    for player in range(0, valid_input_p):
        input_prob_for_this_player = input("\n\tPlease enter how likely (as a percentage value) is Player #" + str(player+1) + " to decide to switch doors (or q to quit):  ")
        valid_input_prob_for_this_player = intInput(input_prob_for_this_player)
        while ((valid_input_prob_for_this_player < 0) or (valid_input_prob_for_this_player > 100)):
            print("\n\tThe input value for Player #" + str(player) + "'s likelihood of deciding to switch doors must be an integer between 0 and 100 (including 0 and 100). ")
            print("\n\tYou have entered a " + str(type(input_prob_for_this_player)) + " of value " + str(input_prob_for_this_player) + ".\n")
            input_prob_for_this_player = input("\n\tPlease enter how likely (as a percentage value) is Player #" + str(player+1) + " to decide to switch doors (or q to quit):  ")
            valid_input_prob_for_this_player = intInput(input_prob_for_this_player)
        list_of_player_switch_probabilities.append(valid_input_prob_for_this_player)
    
    multiplayer_generator.multiplayer_generator(valid_input_n, list_of_player_switch_probabilities, False)
    print("\n\tDone")

def intInput(inp):
    if (inp.rstrip() == 'q'):
        sys.exit()
    try:
        int_inp = int(inp)
    except ValueError:
        try:
            float_inp = float(inp)
        except ValueError:
            return (-1)
        return int(float_inp)
    return int_inp

if __name__ == '__main__':
    main()