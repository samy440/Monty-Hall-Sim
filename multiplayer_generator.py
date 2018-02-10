# import block
from random import randint
import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn-darkgrid')
import numpy as np

def multiplayer_generator(n, players, createFile):

    # Called from the main() function in MHPSim.py
    plt.ion()   # enables interactive mode for plots
    fig = plt.figure()  # initializes the overall plot
    mng = plt.get_current_fig_manager() # used to make the figure apppear in full-screen mode
    mng.resize(*mng.window.maxsize())   # also used to make the figure apppear in full-screen mode
    fig.canvas.set_window_title('Monty Hall Simulator')
    figA = plt.subplot2grid((1, 7), (0, 0), rowspan=1, colspan=4) # figA is the simulation outcome plot
    figA.set_title("Outcome of Simulations\n")
    figA.set_xlabel("Number of Simulations")
    figA.set_ylabel("Cummulative  Success Rate (%)\n(Ending the Simulation with a Car)")
    colours_for_figA = ['red','orange','yellow','green','blue','black','purple','grey','brown']
    labels_list_for_figA = []
    for i in range(0,len(players)):
        labels_list_for_figA.append("Player switching " + str(players[i]) + str('%') + " of time")


    figB = plt.subplot2grid((1, 7), (0, 5), rowspan=1, colspan=2)   # figB is the door distribution plot
    figB.set_title("Distribution of Car Location\n")
    figB.set_xlabel("Door Number")
    figB.set_ylabel("Frequency of Car Location Over " + str(n) + " Simulations (%)")
    plt.ylim([0.0, 100.0])
    x_axis_bar_graph_values = [1, 2, 3]

    car_location_list = [ randint(0, 2) for i in range(n) ] # a list of n integers randomly chosen between [0, 1, 2] representing which door has the car
    car_door_distribution = [0, 0, 0]   # a list representing the distribution of the supposedly random selection of door containing the car
    car_door_distribution_at_sim = np.array(car_door_distribution)

    initial_guess_master_list = []
    random_switch_threshold_list = []
    final_guess_master_list = []
    revealable_doors_master_list = []
    success_rate_master_list = []
    for p in range(0,len(players)):
        initial_guess_master_list.append([ randint(0, 2) for i in range(0, n) ])
        final_guess_master_list.append([])
        success_rate_master_list.append([])
        revealable_doors_master_list.append([])
    rects = figB.bar(x_axis_bar_graph_values, car_door_distribution_at_sim, align='center', alpha=0.5)
    for sim in range(0, n):
        total_iterations_so_far = sim + 1

        switch_threshold = randint(0,100)
        random_switch_threshold_list.append(switch_threshold)

        car_door_distribution[car_location_list[sim]] += (1.0/n)*100
        car_door_distribution_at_sim = np.array(car_door_distribution)
        for rect, h in zip(rects, car_door_distribution_at_sim):
            rect.set_height(h)
            
        fig.canvas.draw()

        monty_reveals = [ 0 for x in range(0,len(players)) ]

        for p in range(0, len(players)):
            revealable_doors_master_list[p] = [ x for x in [0,1,2] if ((x != car_location_list[sim]) and (x != initial_guess_master_list[p][sim])) ]
            monty_reveals[p] = randint(0,(len(revealable_doors_master_list[p])-1))
            if players[p] < switch_threshold:
                switch_guess_list = [ y for y in [0,1,2] if ((y != revealable_doors_master_list[p][monty_reveals[p]]) and (y != initial_guess_master_list[p][sim])) ]
                if len(switch_guess_list) == 1:
                    final_guess_master_list[p].append(switch_guess_list[0])
                else:
                    rndpick = randint(0,(len(switch_guess_list)-1))
                    final_guess_master_list[p].append(switch_guess_list[rndpick])
                final_guess_master_list[p].append( y for y in [0,1,2] if ((y != revealable_doors_master_list[p][monty_reveals[p]]) and (y != initial_guess_master_list[p][sim])) )
            else:
                initial_guess = int(initial_guess_master_list[p][sim])
                final_guess_master_list[p].append(initial_guess)
            
            if final_guess_master_list[p][sim] == car_location_list[sim]:
                if sim == 0:
                    success_rate_master_list[p].append(1.0)
                else:
                    success_rate_master_list[p].append( ((success_rate_master_list[p][sim-1]*sim) + 1.0) / total_iterations_so_far )
            else:
                if sim == 0:
                    success_rate_master_list[p].append(0.0)
                else:
                    success_rate_master_list[p].append( ((success_rate_master_list[p][sim-1]*sim) + 0.0) / total_iterations_so_far )
        for p in range(0, len(players)):
            figA.scatter(total_iterations_so_far, success_rate_master_list[p][sim]*100, color=colours_for_figA[p])
        plt.pause(0.001)
    
    for p in range(0, len(players)):
        figA.plot( [ x for x in range(1, (n+1))], [ (y*100) for y in success_rate_master_list[p] ], color=colours_for_figA[p], label=labels_list_for_figA[p] )    
    figA.legend(loc='best')
    

    if createFile:
        outfile = open("MHPSim outfile.txt", "w")
        header = "Sim\tCar Door\t"
        for p in range(0,(len(players)-1)):
            pnumber = p + 1
            initialguess = "Player#" + str(pnumber) + "_i" 
            finalguess = "Player#" + str(pnumber) + "_f"
            successrate = "Player#" + str(pnumber) + "_csr"
            header += initialguess + "\t" + finalguess + "\t" + successrate + "\t"
        outfile.write(header + '\n')
        for i in range(0,n):
            line = "Sim#" + str((i+1)) + '\t'
            line += str(car_location_list[i]) + '\t' 
            for p in range(0,(len(players)-1)):
                line += str(initial_guess_master_list[p][i]) + '\t' + str(final_guess_master_list[p][i]) + '\t' + str(success_rate_master_list[p][i]) + '\t'
            line += '\n'
            outfile.write(line)
        outfile.close()
    plt.pause(60)
    

if __name__ == '__main__':
    multiplayer_generator()