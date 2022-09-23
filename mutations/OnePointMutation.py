import random
from copy import deepcopy

from models.Population import Population
from utils.Config import Config
from utils.binary_string_length import binary_string_length


class OnePointMutation:
    mutation_chance_percent = 0
    config = None

    def __init__(self, config: Config):
        self.mutation_chance_percent = config.mutation_chance_percent
        self.config = config

    def mutate(self, population: Population):
        new_generation = deepcopy(population)
        for i in range(len(population.individuals)):
            mutation_probability = random.random()
            if mutation_probability <= self.mutation_chance_percent:
                random_max_val = binary_string_length(self.config.right_limit,
                                                      self.config.left_limit,
                                                      self.config.significant_figures) - 1
                mutation_index_1 = random.randint(0, random_max_val)
                mutation_index_2 = random.randint(0, random_max_val)
                new_generation.individuals[i].chromosome.x[mutation_index_1] = 1 - population.individuals[
                    i].chromosome.x[mutation_index_1]
                new_generation.individuals[i].chromosome.y[mutation_index_2] = 1 - population.individuals[
                    i].chromosome.y[mutation_index_2]
        return new_generation
