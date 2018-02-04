# import block
from random import randint
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')

def generator(n, createFile):
    # Called from the main() function in MHPSim.py
    plt.ion()   # enables interactive mode for plots
    fig = plt.figure()  # initializes the overall plot
    mng = plt.get_current_fig_manager() # used to make the figure apppear in full-screen mode
    mng.resize(*mng.window.maxsize())   # also used to make the figure apppear in full-screen mode
    figA = plt.subplot2grid((1, 7), (0, 0), rowspan=1, colspan=4) # figA is the simulation outcome plot
    figA.set_title("Outcome of Simulations\n")
    figA.set_xlabel("Number of Simulations")
    figA.set_ylabel("Cummulative  Success Rate (%)\n(Ending the Simulation with a Car)")

    figB = plt.subplot2grid((1, 7), (0, 5), rowspan=1, colspan=2)   # figB is the door distribution plot
    figB.set_title("Distribution of Car Location\n")
    figB.set_xlabel("Door Number")
    figB.set_ylabel("Frequency of Car Location Over " + str(n) + " Simulations (%)")
    plt.ylim([0.0, 100.0])
    x_axis_bar_graph_values = [1, 2, 3]

    car_location_list = [ randint(0, 2) for i in range(n) ] # a list of n integers randomly chosen between [0, 1, 2] representing which door has the car
    initial_guess_list = [ randint(0, 2) for i in range(n) ]    # a list of n integers randomly chosen between [0, 1, 2] representing the contestant's initial door-pick
    switched_guess_list = [ ]   # a list which will be populated to contain the n integers representing the contestant's switched door-pick
    switched_outcome = [ 0 for i in range(n) ]  # a list which will be updated to contain the outcome (car/no car == 1/0) of switching the door-pick in the current simulation
    stayed_outcome = [ 0 for i in range(n) ]    # a list which will be updated to contain the outcome (car/no car == 1/0) of staying with the original door-pick in the current simulation
    stayed_outcome_tally = 0.0
    stayed_outcome_tally_list = [ ]
    switched_outcome_tally = 0.0
    switched_outcome_tally_list = [ ]
    car_door_distribution = [0, 0, 0]   # a list representing the distribution of the supposedly random selection of door containing the car
    car_door_distribution_at_sim = np.array(car_door_distribution)
        
    rects = figB.bar(x_axis_bar_graph_values, car_door_distribution_at_sim, align='center', alpha=0.5)

    for sim in range(0, n):
        total_iterations_so_far = (sim + 1) 

        car_door_distribution[car_location_list[sim]] += (1.0/n)*100
        car_door_distribution_at_sim = np.array(car_door_distribution)
        for rect, h in zip(rects, car_door_distribution_at_sim):
            rect.set_height(h)
        fig.canvas.draw()

        revealable_doors = [ x for x in [0,1,2] if ((x != car_location_list[sim]) and (x != initial_guess_list[sim])) ]
        monty_reveals = randint(0,(len(revealable_doors)-1))
        switched_guess_list.append( [ y for y in [0,1,2] if ((y != revealable_doors[monty_reveals]) and (y != initial_guess_list[sim]))] )
        if initial_guess_list[sim] == car_location_list[sim]:
            stayed_outcome[sim] = 1
            stayed_outcome_tally *= sim
            stayed_outcome_tally += 1.0
            stayed_outcome_tally /= total_iterations_so_far
            stayed_outcome_tally_list.append(stayed_outcome_tally)
            switched_outcome_tally *= sim
            switched_outcome_tally /= total_iterations_so_far
            switched_outcome_tally_list.append(switched_outcome_tally)
        if switched_guess_list[sim][0] == car_location_list[sim]:
            switched_outcome[sim] = 1
            switched_outcome_tally *= sim
            switched_outcome_tally += 1.0
            switched_outcome_tally /= total_iterations_so_far
            switched_outcome_tally_list.append(switched_outcome_tally)
            stayed_outcome_tally *= sim
            stayed_outcome_tally /= total_iterations_so_far
            stayed_outcome_tally_list.append(stayed_outcome_tally)
        figA.scatter(total_iterations_so_far, stayed_outcome_tally_list[sim]*100, color='red')
        figA.scatter(total_iterations_so_far, switched_outcome_tally_list[sim]*100, color='blue')

    figA.plot([ x for x in range(1, (n+1))], [ (y*100) for y in stayed_outcome_tally_list ], color='red', label='Always Stay')
    figA.plot([ x for x in range(1, (n+1))], [ (y*100) for y in switched_outcome_tally_list ], color='blue', label='Always Switch')
    figA.legend(loc='best')
    plt.pause(60)

    if createFile:
        MHPSim_record = open("MHPSim_record.csv","w")
        MHPSim_record.write("[Simulation Number],[Car Location (1/2/3)],[Initial Guess (1/2/3)],[Switch Guess (1/2/3)],[Stayed Outcome (1/0)],[Switched Outcome (1/0)]\n")
        for x in range(0,len(car_location_list)):
            MHPSim_record.write(str(x+1) + "," + str((car_location_list[x])+1) + "," + str((initial_guess_list[x])+1) + "," + str((switched_guess_list[x][0])+1) + "," + str(stayed_outcome[x]+1) + "," + str(switched_outcome[x]+1) + "\n")
        MHPSim_record.close()

if __name__ == '__main__':
    generator()