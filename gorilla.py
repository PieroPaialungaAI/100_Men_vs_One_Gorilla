import numpy as np 
from constants import * 
class Gorilla:
    def __init__(self, avg_strength = AVG_GORILLA_STRENGTH, std_strength = STD_GORILLA_STRENGTH, avg_resistance = AVG_GORILLA_RESISTANCE, std_resistance = STD_GORILLA_RESISTANCE):
        self.strength = np.random.normal(loc=avg_strength, scale = std_strength, size = 1)[0]
        self.resistance = np.random.normal(loc=avg_strength, scale = std_strength, size = 1)[0]
        self.alive = True


    def take_damage(self, human_strength):
        damage_value = (human_strength/self.resistance)*CONVERSION_CONSTANT
        self.resistance = self.resistance - damage_value
        self.alive = (self.resistance>0)


    def take_damage_batch(self, population, batch_factor = True):
        human_batch = population.batch
        for human in human_batch:
            if batch_factor:
                self.take_damage(human.strength*len(human_batch))
            else:
                self.take_damage(human.strength)
            if self.alive is False:
                break


