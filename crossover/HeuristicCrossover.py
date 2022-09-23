from models.Population import Population
from utils.Config import Config
from copy import deepcopy
import random
import math


class HeuristicCrossover:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def crossover(self, decimal_population: Population):
        next_generation = []
        number_of_population = self.config.number_of_population
        crossover_chance_percent = self.config.crossover_chance_percent

        while len(next_generation) < number_of_population:
            current_generation = deepcopy(decimal_population)
            index_no_1 = random.randint(0, len(current_generation.individuals) - 1)
            index_no_2 = random.randint(0, len(current_generation.individuals) - 1)
            crossover_probability = random.random()
            k_parameter = random.random()

            if crossover_probability <= crossover_chance_percent and current_generation.individuals[
                index_no_1].chromosome.x > \
                    current_generation.individuals[index_no_2].chromosome.x and current_generation.individuals[
                index_no_1].chromosome.y > \
                    current_generation.individuals[index_no_2].chromosome.y:
                next_generation.append((k_parameter * (
                        current_generation.individuals[index_no_1].chromosome.x - current_generation.individuals[
                    index_no_2].chromosome.x) +
                                        current_generation.individuals[index_no_2].chromosome.x, k_parameter * (
                                                current_generation.individuals[index_no_1].chromosome.y -
                                                current_generation.individuals[index_no_2].chromosome.y) +
                                        current_generation.individuals[index_no_2].chromosome.y))
            elif crossover_probability <= crossover_chance_percent and current_generation.individuals[
                index_no_1].chromosome.x < \
                    current_generation.individuals[index_no_2].chromosome.x and current_generation.individuals[
                index_no_1].chromosome.y < \
                    current_generation.individuals[index_no_2].chromosome.y:
                next_generation.append((k_parameter * (
                        current_generation.individuals[index_no_2].chromosome.x - current_generation.individuals[
                    index_no_1].chromosome.x) +
                                        current_generation.individuals[index_no_1].chromosome.x, k_parameter * (
                                                current_generation.individuals[index_no_2].chromosome.y -
                                                current_generation.individuals[index_no_1].chromosome.y) +
                                        current_generation.individuals[index_no_1].chromosome.y))

        return Population.from_tuple_list(next_generation[:len(next_generation) - math.ceil(
            self.config.number_of_population * self.config.elite_percent)])
