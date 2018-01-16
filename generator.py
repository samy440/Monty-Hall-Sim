# Add description

from random import randint

def generator(n):

    MHPSim_temp_stay = open("MHPSim_temp_stay.csv", "w")
    MHPSim_temp_switch = open("MHPSim_temp_switch.csv", "w")
    # open a stats file?

    car_location_list = [ randint(0,2) for i in range(n) ]
    initial_guess_list = [ randint(0,2) for i in range(n) ]
    switched_guess_list = [ ]
    switched_outcome = [ 0 for i in range(n) ]
    stayed_outcome = [ 0 for i in range(n) ]
    for iter in range(0,n):
        outcome = 0
        revealable_doors = [ x for x in [0,1,2] if ((x != car_location_list[iter]) and (x != initial_guess_list[iter])) ]
        monty_reveals = randint(0,len(revealable_doors))
        switched_guess_list.append( [ y for y in revealable_doors if (y != monty_reveals) ] )
        if initial_guess_list[iter] == car_location_list[iter]:
            stayed_outcome[iter] = 1
        if switched_guess_list[iter] == car_location_list[iter]:
            switched_outcome[iter] = 1
        MHPSim_temp_stay.write('\n' + str(stayed_outcome[iter]) + "," + str(initial_guess_list[iter]) + "," + str(car_location_list[iter]))
        MHPSim_temp_switch.write('\n' + str(switched_outcome[iter]) + "," + str(switched_guess_list[iter]) + "," + str(car_location_list[iter]))
    MHPSim_temp_stay.close()
    MHPSim_temp_switch.close()
        
if __name__ == '__main__':
    generator()