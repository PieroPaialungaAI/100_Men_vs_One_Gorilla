from constants import * 
import numpy as np
from human import Human

class HumanPopulation:
    def __init__(self, men_number = MEN_NUMBER, strategy  = None, batch_number = DEFAULT_BATCH_MEN):
        self.N = men_number
        self.population = []
        for _ in range(self.N):
            human = Human()
            self.population.append(human)
        self.batch_number = batch_number
        self.population_strength = [human.strength.copy() for human in self.population]
        self.population_resistance = [human.resistance.copy() for human in self.population]
        self.population_fitness = [human.strength.copy()+human.resistance.copy() for human in self.population]
        self.strategy = strategy
        self.order = list(range(men_number))
        self.order_by_strategy()
        self.build_batches()
        self.no_more_men = False
        self.remaining_men = len(self.population)

    
    def order_by_strategy(self):
        if self.strategy is None:
            return None

        if self.strategy == 'resistance_first':
            self.order = np.argsort(self.population_resistance)[::-1]

        elif self.strategy == 'strength_first':
            self.order = np.argsort(self.population_strength)[::-1]
        
        elif self.strategy == 'fitness_first':
            self.order = np.argsort(self.population_fitness)[::-1]

        new_population = []
        new_strength_list = []
        new_resistance_list = []
        for i in self.order:
            new_population.append(self.population[i])
            new_strength_list.append(self.population_strength[i])
            new_resistance_list.append(self.population_resistance[i])
        self.population = new_population
        self.population_strength = new_strength_list
        self.population_resistance = new_resistance_list


    def build_batches(self):
        self.batches = []
        batch_count = self.N // self.batch_number
        count = 0
        for i in range(batch_count):
            self.batches.append([self.population[k] for k in range(count, min(self.N,count+self.batch_number))])
            count += self.batch_number
        self.batch_count = len(self.batches)
        self.batch_i = 0
        self.batch = self.batches[self.batch_i]
        
            
    def take_damage(self, gorilla, print_statement = True):
        if len(self.batch) == 0:
            if self.batch_i == self.batch_count-1:
                self.no_more_men = True
                return None 
            else:
                if print_statement:
                    print('We ended the batch, going to the next one')
                self.batch_i += 1
                self.batch = self.batches[self.batch_i]
        
        else:
            newbatch = []
            self.gorilla_strength_array = np.random.choice(100,size = len(self.batch))
            self.gorilla_strength_array = self.gorilla_strength_array/self.gorilla_strength_array.max()
            self.gorilla_strength_array = self.gorilla_strength_array * gorilla.strength
            start_men = self.remaining_men
            for i,human in enumerate(self.batch):
                if print_statement:
                    print(f'Processing human {i}, out of {len(self.batch)}')
                damage_value = (self.gorilla_strength_array[i]/human.resistance)*CONVERSION_CONSTANT
                human.resistance = human.resistance - damage_value
                human.alive = (human.resistance>0)
                if human.alive:
                    if print_statement:
                        print(f'Human is alive with resistance {human.resistance}')
                    newbatch.append(human)
                else:
                    self.remaining_men -= 1
            
            self.batch = newbatch
            if print_statement:
                print(f'We lost {start_men-self.remaining_men} man, batch size is now {len(self.batch)}')



    



