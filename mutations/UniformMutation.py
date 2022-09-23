import random
from copy import deepcopy

from models.Individual import Individual
from models.Population import Population
from utils.Config import Config


class UniformMutation:
    mutation_chance_percent = 0
    config = None

    def __init__(self, config: Config):
        self.mutation_chance_percent = config.mutation_chance_percent
        self.config = config

    def mutate(self, decimal_population: Population):
        next_generation = []
        current_generation = deepcopy(decimal_population)
        for i in range(len(current_generation.individuals)):
            mutation_probability = random.random()
            if mutation_probability <= self.mutation_chance_percent:
                mutation_index = random.randint(0, 1)
                if mutation_index == 0:
                    next_generation.append(
                        Individual.from_tuple((random.uniform(-10, 10), current_generation.individuals[i].chromosome.y))
                    )
                elif mutation_index == 1:
                    next_generation.append(
                        Individual.from_tuple(
                            (current_generation.individuals[i].chromosome.x,
                             random.uniform(self.config.left_limit, self.config.right_limit))
                        )
                    )
            else:
                next_generation.append(current_generation.individuals[i])

        return Population(next_generation)
