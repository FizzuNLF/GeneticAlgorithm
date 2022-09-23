import random
from copy import deepcopy

import math

from models.Population import Population
from utils.Config import Config


class UniformCrossover:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def crossover(self, binary_population: Population):
        next_generation = []
        current_generation = deepcopy(binary_population)
        random_max_val = len(binary_population.individuals) - 1

        while len(next_generation) != self.config.number_of_population:
            mutation_index_1 = random.randint(0, random_max_val)
            mutation_index_2 = random.randint(0, random_max_val)

            binary_population.individuals[mutation_index_1].chromosome.x, binary_population.individuals[
                mutation_index_2].chromosome.x = self.u_crossover(
                binary_population.individuals[mutation_index_1].chromosome.x,
                binary_population.individuals[mutation_index_1].chromosome.x,
                self.config.crossover_chance_percent
            )
            binary_population.individuals[mutation_index_1].chromosome.y, binary_population.individuals[
                mutation_index_2].chromosome.y = self.u_crossover(
                binary_population.individuals[mutation_index_1].chromosome.y,
                binary_population.individuals[mutation_index_1].chromosome.y,
                self.config.crossover_chance_percent
            )
            next_generation.append(current_generation.individuals[mutation_index_1])
            if len(next_generation) != self.config.number_of_population:
                next_generation.append(current_generation.individuals[mutation_index_2])

        return Population(next_generation[:len(next_generation) - math.ceil(
            self.config.number_of_population * self.config.elite_percent)])

    def u_crossover(self, ch1, ch2, probability):
        size = min(len(ch1), len(ch2))
        for i in range(size):
            if random.random() < probability:
                ch1[i], ch2[i] = ch2[i], ch1[i]

        return ch1, ch2
