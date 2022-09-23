from copy import deepcopy
import random

import math

from models.Population import Population
from utils.Config import Config


class TwoPointCrossover:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def crossover(self, binary_population: Population):
        next_generation = []
        current_generation = deepcopy(binary_population)
        random_max_val = len(binary_population.individuals) - 1

        while len(next_generation) != self.config.number_of_population:
            prob = random.random()
            if prob > self.config.mutation_chance_percent:
                continue

            mutation_index_1 = random.randint(0, random_max_val)
            mutation_index_2 = random.randint(0, random_max_val)

            current_generation.individuals[mutation_index_1].chromosome.x, current_generation.individuals[
                mutation_index_2].chromosome.x = self.do_crossover(
                current_generation.individuals[mutation_index_1].chromosome.x,
                current_generation.individuals[mutation_index_2].chromosome.x)

            current_generation.individuals[mutation_index_1].chromosome.y, current_generation.individuals[
                mutation_index_2].chromosome.y = self.do_crossover(
                current_generation.individuals[mutation_index_1].chromosome.y,
                current_generation.individuals[mutation_index_2].chromosome.y)

            next_generation.append(current_generation.individuals[mutation_index_1])
            if len(next_generation) != self.config.number_of_population:
                next_generation.append(current_generation.individuals[mutation_index_2])

        return Population(next_generation[:len(next_generation) - math.ceil(
            self.config.number_of_population * self.config.elite_percent)])

    def do_crossover(self, ch1, ch2):
        size = min(len(ch1), len(ch2))
        slice_point1 = random.randint(1, size)
        slice_point2 = random.randint(1, size - 1)
        if slice_point2 >= slice_point1:
            slice_point2 += 1
        else:
            slice_point1, slice_point2 = slice_point2, slice_point1

        ch1[slice_point1:slice_point2], ch2[slice_point1:
                                            slice_point2] = ch2[slice_point1:slice_point2], ch1[
                                                                                            slice_point1:slice_point2]
        return ch1, ch2
