# Description:
# This script generates two temporary data files corresponding to
# the switch/stay strategies. These files (MPHSim_temp_stay/switch.csv)
# contain the outcome, final door pick, and car door for each iteration
# according to the following format and type:
# [outcome = boolean], [final door pick = int {0,1,2}], [car door = int {0,1,2}].
# 
# generator.py is meant to be called by the main.py script. 
#
# Future work:  add a stats-compiling function and output file,
#               allow for a random strategy (randomly choose to switch or stay)
#               add a parameter representing the number of doors such that there
#               are >= 3 doors to choose from (but still only one car).

from random import randint

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
style.use('fivethirtyeight')


def generator(n):

    MHPSim_temp_stay = open("MHPSim_temp_stay.csv", "w")
    MHPSim_temp_switch = open("MHPSim_temp_switch.csv", "w")
    MHPSim_success_tally = open("MHPSim_success_tally.csv","w")
    # open a stats file?

    car_location_list = [ randint(0,2) for i in range(n) ]
    initial_guess_list = [ randint(0,2) for i in range(n) ]
    switched_guess_list = [ ]
    switched_outcome = [ 0 for i in range(n) ]
    stayed_outcome = [ 0 for i in range(n) ]
    stayed_outcome_tally = 0.0
    switched_outcome_tally = 0.0
    for iter in range(0,n):
        total_iterations_so_far = (iter + 1)
        revealable_doors = [ x for x in [0,1,2] if ((x != car_location_list[iter]) and (x != initial_guess_list[iter])) ]
        monty_reveals = randint(0,(len(revealable_doors)-1))
        switched_guess_list.append( [ y for y in [0,1,2] if ((y != revealable_doors[monty_reveals]) and (y != initial_guess_list[iter]))] )
        if initial_guess_list[iter] == car_location_list[iter]:
            stayed_outcome[iter] = 1
            stayed_outcome_tally *= iter
            stayed_outcome_tally += 1.0
            stayed_outcome_tally /= total_iterations_so_far
            switched_outcome_tally *= iter
            switched_outcome_tally /= total_iterations_so_far
        if switched_guess_list[iter][0] == car_location_list[iter]:
            switched_outcome[iter] = 1
            switched_outcome_tally *= iter
            switched_outcome_tally += 1.0
            switched_outcome_tally /= total_iterations_so_far
            stayed_outcome_tally *= iter
            stayed_outcome_tally /= total_iterations_so_far
        MHPSim_temp_stay.write('\n' + str(stayed_outcome[iter]) + "," + str(initial_guess_list[iter]) + "," + str(car_location_list[iter]))
        MHPSim_temp_switch.write('\n' + str(switched_outcome[iter]) + "," + str(switched_guess_list[iter]) + "," + str(car_location_list[iter]))
        MHPSim_success_tally.write('\n' + str(stayed_outcome_tally) + "," + str(switched_outcome_tally))
    MHPSim_temp_stay.close()
    MHPSim_temp_switch.close()
    MHPSim_success_tally.close()
    display(n)

def display(n):
    fig = plt.figure()
    plot_data = open("MHPSim_success_tally.csv","r").read()
    datapoints = plot_data.split('\n')
    stayed_ys = []
    switched_ys = []
    for line in datapoints[1:]:
        stayed_y, switched_y = line.split(',')
        stayed_ys.append(stayed_y)
        switched_ys.append(switched_y)
    plt.plot(stayed_ys, 'b-')
    plt.plot(switched_ys, 'g-')
    plt.show()

if __name__ == '__main__':
    generator()