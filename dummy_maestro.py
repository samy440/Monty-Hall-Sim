import generator, os

def main():
    print("Welcome to this Monty Hall Problem Simulator!\nThis program aims to run simulations of the Monty Hall Problem with the stay/switch strategies\nand plot their outcome in real time.\n")
    input_number_of_iterations = input("Please input the number of simulations to run:  ")
    while type(int(input_number_of_iterations)) != int: 
        
        print("The input value for the number of simulations to run must be an integer.")
        print("You have entered a " + str(type(input_number_of_iterations)) + ".\n")
        input_number_of_iterations = input("Please input the number of simulations to run:  ")
    
    generator.generator(int(input_number_of_iterations), True)
    print("Done")

if __name__ == '__main__':
    main()