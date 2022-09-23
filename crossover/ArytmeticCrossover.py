from models.Population import Population
from utils.Config import Config
from copy import deepcopy
import random
import math


class ArithmeticCrossover:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def crossover(self, decimal_population: Population):
        next_generation = []
        current_generation = deepcopy(decimal_population)
        number_of_population = self.config.number_of_population
        max_iter = number_of_population
        while len(next_generation) < max_iter:
            index_no_1 = random.randint(0, len(current_generation.individuals) - 1)
            index_no_2 = random.randint(0, len(current_generation.individuals) - 1)
            crossover_probability = random.random()
            if crossover_probability <= self.config.crossover_chance_percent and index_no_1 != index_no_2:
                k_parameter = random.random()
                new = [(
                    k_parameter * current_generation.individuals[index_no_1].chromosome.x + (1 - k_parameter) *
                    current_generation.individuals[index_no_2].chromosome.x,
                    k_parameter * current_generation.individuals[index_no_1].chromosome.y + (1 - k_parameter) *
                    current_generation.individuals[index_no_2].chromosome.y)
                    , (
                        (1 - k_parameter) * current_generation.individuals[index_no_1].chromosome.x + k_parameter *
                        current_generation.individuals[index_no_2].chromosome.x,
                        (1 - k_parameter) * current_generation.individuals[index_no_1].chromosome.y + k_parameter *
                        current_generation.individuals[index_no_2].chromosome.y)
                ]
                if len(next_generation) <= number_of_population - 2:
                    next_generation.append(new[0])
                    next_generation.append(new[1])
                elif len(next_generation) <= number_of_population - 1:
                    next_generation.append(new[0])

        return Population.from_tuple_list(next_generation[:len(next_generation) - math.ceil(
            self.config.number_of_population * self.config.elite_percent)])
