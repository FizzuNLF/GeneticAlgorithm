import random
from copy import deepcopy

import math

from models.Population import Population
from utils.Config import Config
from utils.binary_string_length import binary_string_length


class OnePointCrossover:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def crossover(self, population: Population):
        next_generation = []
        while len(
                next_generation) < self.config.number_of_population:
            current_generation = deepcopy(population)
            index_no_1 = random.randint(0, len(current_generation.individuals) - 1)
            index_no_2 = random.randint(0, len(current_generation.individuals) - 1)
            crossover_probability = random.random()
            if crossover_probability <= self.config.crossover_chance_percent and index_no_1 != index_no_2:
                max_index = binary_string_length(self.config.right_limit,
                                                 self.config.left_limit,
                                                 self.config.significant_figures) - 1
                crossover_index = random.randint(1, max_index)
                for i in range(crossover_index):
                    current_generation.individuals[index_no_1].chromosome.x[i], \
                    current_generation.individuals[index_no_2].chromosome.x[i] = \
                        current_generation.individuals[index_no_2].chromosome.x[i], \
                        current_generation.individuals[index_no_1].chromosome.x[i]

                    current_generation.individuals[index_no_1].chromosome.y[i], \
                    current_generation.individuals[index_no_2].chromosome.y[i] = \
                        current_generation.individuals[index_no_2].chromosome.y[i], \
                        current_generation.individuals[index_no_1].chromosome.y[i]

                if len(
                        next_generation) <= self.config.number_of_population  - 2:
                    next_generation.append(deepcopy(current_generation.individuals[index_no_1]))
                    next_generation.append(deepcopy(current_generation.individuals[index_no_2]))
                elif len(
                        next_generation) <= self.config.number_of_population - 1:
                    next_generation.append(deepcopy(current_generation.individuals[index_no_1]))
                else:
                    break
        return Population(next_generation[:len(next_generation) - math.ceil(
            self.config.number_of_population * self.config.elite_percent)])
