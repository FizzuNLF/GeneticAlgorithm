import random
from copy import deepcopy

import math

from models.Population import Population
from utils.Config import Config


class ThreePointCrossover:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def crossover(self, binary_population: Population):
        next_generation = []
        current_generation = deepcopy(binary_population)
        random_max_val = len(binary_population.individuals) - 1
        random_cross_max_val = len(current_generation.individuals[0].chromosome.x)
        while len(next_generation) != self.config.number_of_population:
            prob = random.random()
            if prob > self.config.mutation_chance_percent:
                continue

            mutation_index_1 = random.randint(0, random_max_val)
            mutation_index_2 = random.randint(0, random_max_val)

            n1 = random.randint(0, random_cross_max_val - 1)
            n2 = random.randint(0, random_cross_max_val - 1)
            n3 = random.randint(0, random_cross_max_val - 1)

            current_generation.individuals[mutation_index_1].chromosome.x, current_generation.individuals[
                mutation_index_2].chromosome.x = self.n_crossover([n1, n2, n3],
                                                                  current_generation.individuals[
                                                                      mutation_index_1].chromosome.x,
                                                                  current_generation.individuals[
                                                                      mutation_index_2].chromosome.x)

            current_generation.individuals[mutation_index_1].chromosome.y, current_generation.individuals[
                mutation_index_2].chromosome.y = self.n_crossover([n1, n2, n3],
                                                                  current_generation.individuals[
                                                                      mutation_index_1].chromosome.y,
                                                                  current_generation.individuals[
                                                                      mutation_index_2].chromosome.y)

            next_generation.append(current_generation.individuals[mutation_index_1])
            if len(next_generation) != self.config.number_of_population:
                next_generation.append(current_generation.individuals[mutation_index_2])

        return Population(next_generation[:len(next_generation) - math.ceil(
            self.config.number_of_population * self.config.elite_percent)])

    def n_crossover(self, n, ch1, ch2):
        n = list(set(n))
        for i in n:
            ch1, ch2 = ch1[:i] + ch2[i:], ch2[:i] + ch1[i:]

        return ch1, ch2
