""""
classes.py

Joshua Goldman 
Final Project 
12/8/23

This program creates the classses for the epidemology and is called upon. Gives the attrbutes for the virus and population
"""
class Disease:
    #creates the diesease class
    def __init__(self, transmission_rate = .5, virulence = 0):
        """intializing the virus transmission rate and virulence"""
        self.transmission_rate = transmission_rate
        self.virulence = virulence

    def get_transmission_rate(self):
        """a get function for transmisssion rate"""
        return self.transmission_rate

    def get_virulence(self):
        """gettign the virulence"""
        return self.virulence

    def set_transmission_rate(self, new_rate):
        """Setting the new transmission rate"""
        self.transmission_rate = new_rate

    def set_virulence(self, new_virulence):
        """setting the new virulence level"""
        self.virulence = new_virulence


#creates a population is the parent class
class Population:
    def __init__(self, transmission_rate, virulence,vaccine_rate):
        """intializing the the parent class and writing method."""
        self.transmission_rate = transmission_rate
        self.virulence = virulence
        self.vaccine_rate = vaccine_rate

    def get_transmission_rate(self):
        """a getter for the transmission rate"""
        return self.transmission_rate

    def set_transmission_rate(self, new_rate):
        """a function that is the setter of transmission rate """
        self.transmission_rate = new_rate

    def set_vaccine_rate(self,vaccine_rate):
        """a function that sets the vaccine rate """
        if 0.0 <= vaccine_rate <= 1.0: #ensuring the vacine rate is in the range of 1. 
            self.vaccine_rate = vaccine_rate
    def get_vaccine_rate(self):
        """a getter for the vacine"""
        return self.vaccine_rate
        

class UrbanPopulation(Population):
    """This a subclass of the population. USES inheritance. """
    def __init__(self, transmission_rate, virulence):
        # Call the __init__ method of the parent class directly
        Population.__init__(self, transmission_rate, virulence, vaccine_rate=0.8)
        #calling the parent class, transmission rate is higher, vaccine complience is higher
        self.urban_factor = 1.2

 

class RuralPopulation(Population):
    def __init__(self, transmission_rate , virulence):
        # Call the __init__ method of the parent class directly
        Population.__init__(self, transmission_rate, virulence, vaccine_rate=0.2)
        #lower rate of vacines and lower transmission
        self.rural_factor = 0.8


class SuburbanPopulation(Population):
    def __init__(self, transmission_rate, virulence):
        # Call the __init__ method of the parent class directly
        Population.__init__(self, transmission_rate, virulence, vaccine_rate=0.5)
        #the control group. urban and rural are based off this. 
        self.suburban_factor = 1.0