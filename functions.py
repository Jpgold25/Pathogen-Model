""""
Functions.py

Joshua Goldman 
Allen Harper


The program has all the functions that the main program calls upon
"""




import random
import graphicsPlus as gr

was_infected = 0  #counters set for keeping track of total affected or infected
was_vaccinated = 0 
died = 0 

def draw_grid(win, rows, cols, box_size):
    """The function creates the grid for the program"""
    boxes = [] #empty list
    for row in range(rows): # a for loop that creates the grid 
        for col in range(cols): #creating the dimesions
            x1 = col * box_size
            y1 = row * box_size
            x2 = x1 + box_size
            y2 = y1 + box_size
            box = gr.Rectangle(gr.Point(x1, y1), gr.Point(x2, y2)) # creates the rectangle
            box.draw(win) #draws the boxes in the window
            boxes.append(box) #adding them to alist 
    return boxes


def applyVaccine(boxes, vaccinate):
    """Iterates through the population and then applies the vaccine to the boxes. Green means a helathy but not vaccinated, blue is vaccianted"""
    global was_vaccinated # creating a global variable
    for box in boxes: #iterating through values
        if random.random() < vaccinate: #if a random number is greater than a populatin vaccinated value, 
            box.setFill("Blue") #making the boxes blue
            was_vaccinated += 1 #incrementing the counter
        else:
            box.setFill("Green") #if not vaccinated it just a normal healty indivial
    return was_vaccinated #returning the counter

def applyVirus(boxes,virus_transmission,transmission_rate_population):
    """Iterating through the population with the virus. The virus has a contagious rate set by paper. vacccinated indivuals have a lower change of getting vaccine"""
    global was_infected #counter
    for box in boxes: #iteration
        if box.getFill() == "Blue": #if vaccinated
            if random.random()*7  < ((transmission_rate_population * virus_transmission)):#vaccinated is 70 effective and decreases the rate of inection
                box.setFill("Red") #infected indicual
                was_infected += 1 # increase counter
        else:
            if random.random() < ((transmission_rate_population * virus_transmission)): #unvaccinated indiviual
                box.setFill("Red") #Infected
                was_infected += 1 
    return was_infected #counter increases


def applyDeath(boxes,virulence):
    """applying a rate of death into the simulation. Death is decided by the virulence"""
    global died
    for box in boxes: #incrementing through population 
        if box.getFill() == "Red": # only apply death rate to infected
            if random.random() < virulence:
                box.setFill("Black")
                died += 1
    return died

