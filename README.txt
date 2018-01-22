This serves as a Monty Hall Problem simulator. 
Here's an overview of the way it works:

main.py
    Handles I/O (asks for the number of iterations, where an iteration is a single Monty Hall Problem).
    Calls generator.py to set up the temporary data files.
    Calls visualise.py to visualize the outcome of the iterations in real-time.

generator.py
    Input from main.py = {n (number of iterations)}.
    Makes the temporary data files (MHPSim_temp_switch.csv and MHPSim_temp_stay.csv).
    Populates the temporary data files using the format
        [pick], [door #1], [door #2], [door #3], [outcome]
    by making the following lists:
        car_location_list = [list of n randomly-generated ints in range [0,1,2]]
        initial_guess_list = [list of n randomly-generated ints in range [0,1,2]]

    For iter = 0 to n:
        monty_reveals = x in [0,1,2] s.t. (x != car_location_list[n]) and (x != initial_guess_list[n])
        if switch then pick = y in [0,1,2] s.t. (y != initial_guess_list[n]) and (y != x)
        if pick == car_location_list[n] then outcome = 1 else outcome = 0
        MHPSim_temp_stay.append(pick + "," + door)





    