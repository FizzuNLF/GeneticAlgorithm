import random
from copy import deepcopy

from models.Population import Population
from utils.Config import Config
from utils.binary_string_length import binary_string_length


class Inversion:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def invert(self, population: Population):
        new_generation = deepcopy(population)
        for i in range(len(population.individuals)):
            inversion_probability = random.random()
            binary_len = binary_string_length(self.config.right_limit,
                                              self.config.left_limit,
                                              self.config.significant_figures)
            max_index = binary_len - 1

            if inversion_probability <= self.config.inversion_chance_percent:
                inversion_index_1 = random.randint(0, max_index)
                inversion_index_2 = random.randint(inversion_index_1, max_index)
                inversion_index_3 = random.randint(0, max_index)
                inversion_index_4 = random.randint(inversion_index_3, max_index)

                temp_x = new_generation.individuals[i].chromosome.x
                temp_x[inversion_index_1:inversion_index_2] = temp_x[inversion_index_1:inversion_index_2][::-1]

                temp_y = new_generation.individuals[i].chromosome.y
                temp_y[inversion_index_3:inversion_index_4] = temp_y[inversion_index_3: inversion_index_4][::-1]

                new_generation.individuals[i].chromosome.x = temp_x
                new_generation.individuals[i].chromosome.y = temp_y
        return new_generation
