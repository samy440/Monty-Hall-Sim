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
from matplotlib import style
import matplotlib
matplotlib.use('TKAgg')
import numpy as np
style.use('fivethirtyeight')

def generator(n, createFile):
    plt.ion()
    fig = plt.figure()
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    figA = plt.subplot2grid((1,7), (0,0), rowspan=1, colspan=4)
    figA.set_title("Outcome of Simulations\n")
    figA.set_xlabel("Number of Simulations")
    figA.set_ylabel("Rate of Success\n(Ending the Simulation with a Car)")

    figB = plt.subplot2grid((1,7), (0,5), rowspan=1, colspan=2)
    figB.set_title("Distribution of Car Location\n")
    figB.set_xlabel("Door Number")
    figB.set_ylabel("Frequency of Holding Car")
    plt.ylim([0.0, 1.0])
    x_axis_bar_graph = ("Door #1", "Door #2", "Door #3")
    x_axis_bar_graph_values = [1,2,3]

    car_location_list = [ randint(0,2) for i in range(n) ]
    initial_guess_list = [ randint(0,2) for i in range(n) ]
    switched_guess_list = [ ]
    switched_outcome = [ 0 for i in range(n) ]
    stayed_outcome = [ 0 for i in range(n) ]
    stayed_outcome_tally = 0.0
    stayed_outcome_tally_list = [ ]
    switched_outcome_tally = 0.0
    switched_outcome_tally_list = [ ]
    car_door_distribution = [0,0,0]
    car_door_distribution_at_iter = np.array(car_door_distribution)
        
    rects = figB.bar(x_axis_bar_graph_values, car_door_distribution_at_iter, align='center', alpha=0.5)

    for iter in range(0,n):
        total_iterations_so_far = (iter + 1)

        car_door_distribution[car_location_list[iter]] += (1.0/n)
        car_door_distribution_at_iter = np.array(car_door_distribution)
        for rect, h in zip(rects, car_door_distribution_at_iter):
            rect.set_height(h)
        fig.canvas.draw()

        revealable_doors = [ x for x in [0,1,2] if ((x != car_location_list[iter]) and (x != initial_guess_list[iter])) ]
        monty_reveals = randint(0,(len(revealable_doors)-1))
        switched_guess_list.append( [ y for y in [0,1,2] if ((y != revealable_doors[monty_reveals]) and (y != initial_guess_list[iter]))] )
        if initial_guess_list[iter] == car_location_list[iter]:
            stayed_outcome[iter] = 1
            stayed_outcome_tally *= iter
            stayed_outcome_tally += 1.0
            stayed_outcome_tally /= total_iterations_so_far
            stayed_outcome_tally_list.append(stayed_outcome_tally)
            switched_outcome_tally *= iter
            switched_outcome_tally /= total_iterations_so_far
            switched_outcome_tally_list.append(switched_outcome_tally)
        if switched_guess_list[iter][0] == car_location_list[iter]:
            switched_outcome[iter] = 1
            switched_outcome_tally *= iter
            switched_outcome_tally += 1.0
            switched_outcome_tally /= total_iterations_so_far
            switched_outcome_tally_list.append(switched_outcome_tally)
            stayed_outcome_tally *= iter
            stayed_outcome_tally /= total_iterations_so_far
            stayed_outcome_tally_list.append(stayed_outcome_tally)
        figA.scatter(total_iterations_so_far, stayed_outcome_tally_list[iter], color='red')
        figA.scatter(total_iterations_so_far, switched_outcome_tally_list[iter], color='blue')
        

        plt.pause(0.005)
    figA.plot([ x for x in range(1, (n+1))], stayed_outcome_tally_list, color='red', label='Always Stay')
    figA.plot([ x for x in range(1, (n+1))], switched_outcome_tally_list, color='blue', label='Always Switch')
    figA.legend(loc='best')
    plt.pause(10)
    if createFile:
        MHPSim_record = open("MHPSim_record.csv","w")
        MHPSim_record.write("[Simulation Number],[Car Location (1/2/3)],[Initial Guess (1/2/3)],[Switch Guess (1/2/3)],[Stayed Outcome (1/0)],[Switched Outcome (1/0)]\n")
        for x in range(0,len(car_location_list)):
            MHPSim_record.write(str(x+1) + "," + str((car_location_list[x])+1) + "," + str((initial_guess_list[x])+1) + "," + str((switched_guess_list[x][0])+1) + "," + str(stayed_outcome[x]+1) + "," + str(switched_outcome[x]+1) + "\n")
        MHPSim_record.close()

if __name__ == '__main__':
    generator()