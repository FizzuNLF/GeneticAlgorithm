import random
from copy import deepcopy
import statistics
from models.Individual import Individual
from models.Population import Population
from utils.Config import Config


class GaussMutation:
    mutation_chance_percent = 0
    config = None

    def __init__(self, config: Config):
        self.mutation_chance_percent = config.mutation_chance_percent
        self.config = config

    def mutate(self, decimal_population: Population):
        next_generation = []
        current_generation = deepcopy(decimal_population)
        x_mean, y_mean = self.mean_calculation(current_generation)
        x_std, y_std = self.std_calculation(current_generation)
        for i in range(len(current_generation.individuals)):
            mutation_probability = random.random()
            if mutation_probability <= self.config.mutation_chance_percent:
                new = (current_generation.individuals[i].chromosome.x + random.gauss(x_mean, x_std),
                       current_generation.individuals[i].chromosome.y + random.gauss(y_mean, y_std))
                if self.config.left_limit <= new[0] <= self.config.right_limit and self.config.left_limit <= new[
                    1] <= self.config.right_limit:
                    next_generation.append(Individual.from_tuple(new))
                else:
                    next_generation.append(current_generation.individuals[i])
            else:
                next_generation.append(current_generation.individuals[i])

        return Population(next_generation)

    # obliczanie średnich ze zbioru
    def mean_calculation(self, decimal_population: Population):
        current_generation = deepcopy(decimal_population)
        x = []
        y = []
        for i in range(len(decimal_population.individuals)):
            x.append(current_generation.individuals[i].chromosome.x)
            y.append(current_generation.individuals[i].chromosome.y)

        return statistics.mean(x), statistics.mean(y)

    # obliczanie średnich ze zbioru
    def std_calculation(self, decimal_population: Population):
        current_generation = deepcopy(decimal_population)
        x = []
        y = []
        for i in range(len(decimal_population.individuals)):
            x.append(current_generation.individuals[i].chromosome.x)
            y.append(current_generation.individuals[i].chromosome.y)

        return statistics.stdev(x), statistics.stdev(y)
