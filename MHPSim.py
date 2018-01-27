import sys, generator

def main():
    print("""Welcome to this Monty Hall Problem Simulator!\n
    This program aims to run simulations of the Monty Hall Problem
     with the stay/switch strategies\nand plot their outcome in 
     real time.\n""")
    input_number_of_iterations = input("Please input the number of simulations to run (or q to quit):  ")
    valid_input = intInput(input_number_of_iterations)
    while (valid_input < 0):
        print("The input value for the number of simulations to run must be an integer.")
        print("You have entered a " + str(type(input_number_of_iterations)) + ".\n")
        input_number_of_iterations = input("Please input the number of simulations to run (or q to quit):  ")
        valid_input = intInput(input_number_of_iterations)
    generator.generator(valid_input, True)
    print("Done")

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