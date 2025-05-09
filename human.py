from constants import * 
import numpy as np

class Human:
    def __init__(self, avg_strength = AVG_HUMAN_STRENGTH, std_strength = STD_HUMAN_STRENGTH, 
                 avg_resistance = AVG_HUMAN_RESISTANCE, std_resistance = STD_HUMAN_RESISTANCE):
        self.strength = np.random.normal(loc=avg_strength, scale = std_strength, size = 1)[0]
        self.strength = max(self.strength,0)
        self.resistance = np.random.normal(loc=avg_strength, scale = std_strength, size = 1)[0]
        self.resistance = max(self.resistance, 0)
        self.alive = True

    
    def take_damage(self, gorilla_strength):
        if self.resistance<0:
            return 
        damage_value = (gorilla_strength/self.resistance)*CONVERSION_CONSTANT
        self.resistance = self.resistance - damage_value
        self.alive = (self.resistance>0)


