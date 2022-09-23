from models.Individual import Individual
from utils.Config import Config
from typing import List
from typing import Tuple


class Population:
    individuals: List[Individual] = []

    def __init__(self, *args):
        if len(args) > 0:
            self.individuals = args[0]

    @staticmethod
    def initialize_random(individuals_number: int, config: Config):
        decimal_population = []
        [decimal_population.append(Individual(config)) for _ in range(individuals_number)]
        return Population(decimal_population)

    @staticmethod
    def from_tuple_list(tuples: List[Tuple[float, float]]):
        ind = []
        [ind.append(Individual.from_tuple(tuple)) for tuple in tuples]
        pop = Population()
        pop.individuals = ind
        return pop
