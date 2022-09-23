import random
from copy import deepcopy

from FitnessFunction.FitnessFunction import function_booth_output
from models.Population import Population
from utils.Config import Config


class Tournament:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def calculate(self, binary_population: Population):
        new_population = deepcopy(binary_population)
        new_generation = []
        random.shuffle(new_population.individuals)
        list_of_tournaments = list(self.list_split(binary_population.individuals, self.config.tournament_gourps_size))
        for i in range(len(list_of_tournaments)):
            function_output = function_booth_output(Population(list_of_tournaments[i]))
            if self.config.maximalization:
                best_fit_index = function_output.index(max(function_output))
            else:
                best_fit_index = function_output.index(min(function_output))
            new_generation.append(list_of_tournaments[i][best_fit_index])
        return Population(new_generation)

    def list_split(self, binary_population, number_of_object_in_single_group):
        for x in range(0, len(binary_population), number_of_object_in_single_group):
            list_part = binary_population[x: number_of_object_in_single_group + x]

            if len(list_part) < number_of_object_in_single_group:
                list_part = list_part
            yield list_part
