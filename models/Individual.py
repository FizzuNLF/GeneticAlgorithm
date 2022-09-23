from models.Chromosome import Chromosome
from utils.Config import Config
from typing import Tuple


class Individual:
    chromosome: Chromosome = None

    def __init__(self, config: Config):
        self.chromosome = Chromosome(config)

    @staticmethod
    def from_tuple(tuple: Tuple[float, float]):
        ind = Individual(None)
        ind.chromosome = Chromosome.from_tuple(tuple)
        return ind
