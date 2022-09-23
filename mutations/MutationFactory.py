from mutations.EdgeMutation import EdgeMutation
from mutations.OnePointMutation import OnePointMutation
from mutations.TwoPointMutation import TwoPointMutation
from mutations.GaussMutation import GaussMutation
from mutations.UniformMutation import UniformMutation
from utils.Config import Config
from enum import Enum


class MutationMethod(Enum):
    OnePoint = 'One point'
    TwoPoints = 'Two points'
    Edge = 'Edge'


class MutationFactory:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def create_mutation_algorithm(self):
        if self.config.mutation_method == 'One point':
            return OnePointMutation(self.config)
        if self.config.mutation_method == 'Two points':
            return TwoPointMutation(self.config)
        if self.config.mutation_method == 'Edge':
            return EdgeMutation(self.config)
        if self.config.mutation_method == 'Gaussian':
            return GaussMutation(self.config)
        if self.config.mutation_method == 'Uniform':
            return UniformMutation(self.config)
