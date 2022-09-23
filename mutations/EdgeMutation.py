import random
from copy import deepcopy

from models.Population import Population
from utils.Config import Config
from utils.binary_string_length import binary_string_length


class EdgeMutation:
    mutation_chance_percent = 0
    config = None

    def __init__(self, config: Config):
        self.mutation_chance_percent = config.mutation_chance_percent
        self.config = config

    def mutate(self, population: Population):
        new_generation = deepcopy(population)
        max_index = binary_string_length(self.config.right_limit,
                                         self.config.left_limit,
                                         self.config.significant_figures) - 1
        for i in range(len(population.individuals)):
            mutation_probability = random.random()
            if mutation_probability <= self.mutation_chance_percent:
                new_generation.individuals[i].chromosome.x[max_index] = 1 - new_generation.individuals[i].chromosome.x[
                    max_index]
                new_generation.individuals[i].chromosome.y[max_index] = 1 - new_generation.individuals[i].chromosome.y[
                    max_index]
        return new_generation
