This serves as a Monty Hall Problem simulator. 
Here's an overview of the way it works:

MHPSim.py
    Input:
        None
    Tasks:
        Handles I/O (asks for the number of iterations, where an iteration is a single Monty Hall Problem).
        Calls generator.py to set up the temporary data files.

generator.py
    Input:
        Input from MHPSim.py = {n (number of iterations), createFile (True/False)}.
    Tasks:
        Makes a window for the sim's graphs (fig).
        Resizes the window to be full-screen.
        # Bug: if I move the window during the simulation, it freezes.
        Runs and plots the simulations.
    Variables:
        figA is the scatter/line plot that shows the cumulative success rate of the strategy (Switch/Stay).
        figB is a histogram showing the frequency with which each door is set to hold the car.
        car_location_list is a list of n-elements where each element a randomly chosen element of the set (0, 1, 2) .
        car_location_list represents which door has the car at each iteration/simulation.
        initial_guess_list is a list of n-elements where each element a randomly chosen element of the set (0, 1, 2).
        initial_guess_list represents which door was initially picked by the player at each iteration/simulation.
        switched_guess_list is a list of n-elements that is initially empty, but will be populated by the number (0, 1, 2) of the door the contestant decides to switch to.
            (needs to be empty at first because the door Monty reveals (see later) for each simulation is not predetermined.)
        switched_outcome is a list of n 0s representing the outcome of each simulation (the ith 0 becomes a 1 if the simulation where the player switches is successful).
        stayed_outcome is a list of n 0s representing the outcome of each simulation (the ith 0 becomes a 1 if the simulation where the player stays is successful).
        stayed_outcome_tally holds the cumulative success rate of the "stay" strategy over all simulations completed this far.
        stayed_outcome_tally_list is a list of n-elements containing the n successive values of stayed_outcome_tally in order (is used to generate the scatter plot).
        switched_outcome_tally holds the cumulative success rate of the "switch" strategy over all simulations completed this far.
        switched_outcome_tally_list is a list of n-elements containing the n successive values of stayed_outcome_tally in order (is used to generate the scatter plot).
        car_door_distribution is a list of 3 real numbers representing the cumulative frequency of having the car behind each of the three doors over the n simulations.







    