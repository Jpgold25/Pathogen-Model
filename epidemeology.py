""""
epidemology.py

Joshua Goldman 
Allen Harper
Final Project
How to run: epidemeology.py, answer the prompt with one of three choices

The program creates a visual repersentation of a virus going through a population. The amount infected changes based off difffernt populations
"""


import graphicsPlus as gr
import sys
import random
import classes as CL
import functions as F

def main():
    """The main function calls upon all other function and creates the simulation"""

        # Ask the user a question
    user_choice = input("Choose a location type (rural, suburbs, urban): ")

    # Validate the user's choice
    if user_choice not in ["rural", "suburbs", "urban"]:
        print("Invalid location type. Choose 'rural', 'suburbs', or 'urban'.")
        sys.exit(1)
    

    # Set the size of each box and the number of rows and columns
    box_size = 20
    rows = 20
    cols = 20
    

    # Calculate the window size based on the grid size
    win_width = cols * box_size
    win_height = rows * box_size


    # Create a GraphWin object
    win = gr.GraphWin("Virus Model", win_width, win_height)
 

    # Draw the grid and get the list of boxes
    boxes = F.draw_grid(win, rows, cols, box_size)

    # Change the color of all boxes to red
    if user_choice == "rural":
        population = CL.RuralPopulation(.5, 0)
    elif user_choice == "suburbs":
        population = CL.SuburbanPopulation(1, 0)
    elif user_choice == "urban":
        population =CL.UrbanPopulation(1.2, 0)
    else:
        print("Invalid location type.")
        sys.exit(1)

    
    # Get the vaccine rate for the selected population
    vaccine_rate = population.get_vaccine_rate()
    disease = CL.Disease(transmission_rate= .5, virulence=.3) #making virus
    virus_rate = disease.get_transmission_rate() #extracting values
    virulence = disease.get_virulence() #extracting cirulence
    population_transmission = population.get_transmission_rate()
    # Change the color of boxes based on the vaccine rate
    F.applyVaccine(boxes, vaccine_rate) 
    #applying the virus rate to the population
    F.applyVirus(boxes,virus_rate,population_transmission)
    #applying the death rate to the population 
    F.applyDeath(boxes,virulence)


    #Present all the data 
    print("Virus Rate:", virus_rate)
    print("Population Transmission:", population_transmission)
    print("Was Vaccinated:", F.was_vaccinated)
    print("Was Infected:", F.was_infected)
    print("Died:", F.died)
    
    

    # Wait for a click to close the window
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()





