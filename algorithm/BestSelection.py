from copy import deepcopy

import math

from FitnessFunction.FitnessFunction import function_booth, function_booth_output
from models.Population import Population
from utils.Config import Config


class BestSelection:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def calculate(self, binary_population: Population):
        new_population = deepcopy(binary_population)
        best_population_individuals = self.fit_selection(new_population, self.config.selection_percent)

        return Population(best_population_individuals)

    def fit_selection(self, binary_population: Population, percent):
        list_of_elements = function_booth_output(binary_population)
        list_of_selected_object = []
        for i in range(math.ceil(len(binary_population.individuals) * percent)):
            if self.config.maximalization:
                minimum_value_fit_index = list_of_elements.index(min(list_of_elements))
                maximum_value_fit_index = list_of_elements.index(max(list_of_elements))
                list_of_selected_object.append(binary_population.individuals[maximum_value_fit_index])
                list_of_elements[maximum_value_fit_index] = list_of_elements[minimum_value_fit_index]
            else:
                minimum_value_fit_index = list_of_elements.index(min(list_of_elements))
                maximum_value_fit_index = list_of_elements.index(max(list_of_elements))
                list_of_selected_object.append(binary_population.individuals[minimum_value_fit_index])
                list_of_elements[minimum_value_fit_index] = list_of_elements[maximum_value_fit_index]
        return list_of_selected_object
