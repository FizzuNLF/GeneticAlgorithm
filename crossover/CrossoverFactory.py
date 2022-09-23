from enum import Enum

from crossover.OnePointCrossover import OnePointCrossover
from crossover.ThreePointCrossover import ThreePointCrossover
from crossover.TwoPointCrossover import TwoPointCrossover
from crossover.UniformCrossover import UniformCrossover
from crossover.ArytmeticCrossover import ArithmeticCrossover
from crossover.HeuristicCrossover import HeuristicCrossover
from utils.Config import Config


class CrossType(Enum):
    OnePoint = 'One point'
    TwoPoints = 'Two points'
    ThreePoints = 'Three points'
    Homo = 'Homo'


class CrossoverFactory:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def create_crossover(self):
        tmp = self.config.cross_method
        if tmp == 'One point':
            return OnePointCrossover(self.config)
        if tmp == 'Two points':
            return TwoPointCrossover(self.config)
        if tmp == 'Three points':
            return ThreePointCrossover(self.config)
        if tmp == 'Homo':
            return UniformCrossover(self.config)
        if tmp == 'Arithmetic':
            return ArithmeticCrossover(self.config)
        if tmp == 'Heuristic':
            return HeuristicCrossover(self.config)
