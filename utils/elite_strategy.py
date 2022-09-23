import math

from FitnessFunction.FitnessFunction import function_booth_output
from models.Population import Population
from utils.Config import Config


def elite_strategy(binary_population: Population, config: Config):
    return fit_selection(binary_population, config)


def fit_selection(population: Population, config: Config):
    percent = config.elite_percent
    list_of_elements = function_booth_output(population)
    list_of_selected_object = []
    for i in range(math.ceil(len(population.individuals) * percent)):
        if config.maximalization:
            minimum_value_fit_index = list_of_elements.index(min(list_of_elements))
            maximum_value_fit_index = list_of_elements.index(max(list_of_elements))
            list_of_selected_object.append(population.individuals[maximum_value_fit_index])
            list_of_elements[maximum_value_fit_index] = list_of_elements[minimum_value_fit_index]
        else:
            minimum_value_fit_index = list_of_elements.index(min(list_of_elements))
            maximum_value_fit_index = list_of_elements.index(max(list_of_elements))
            list_of_selected_object.append(population.individuals[minimum_value_fit_index])
            list_of_elements[minimum_value_fit_index] = list_of_elements[maximum_value_fit_index]
    return Population(list_of_selected_object)
