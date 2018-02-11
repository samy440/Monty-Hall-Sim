This program serves as a Monty Hall Problem simulator. 
I used it as a hands-on way to become familiar with matplotlib
and with some basic elements of interactive plotting (the latter
might come in very handy when I start with machine learning 
projects).
Here's an overview of the way it works:

MHPSim.py
    Input:
        None
    Tasks:
        Handles I/O:
            Asks for the number of iterations (where an iteration is a single Monty Hall Problem).
            Asks for the number (1 to 9, inclusive) of independent players to simulate.
            Asks for the rate at which every individual player decides to switch its guess (as a percentage value).
            Can always hit the 'q' key to exit the program.
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
        revealable_doors is a list of n integers representing which door(s) Monty CAN reveal at each simulation.
            Monty can only reveal doors that A) the player hasn't chosen as their initial guess, and B) do not have the car.
        monty_reveals represents the door that Monty reveals.    