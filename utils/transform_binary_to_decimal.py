from models.Population import Population
from utils.Config import Config
from utils.binary_string_length import binary_string_length
from utils.list_to_string import list_to_string


def binary_to_decimal(val):
    return int(val, 2)


def transform_binary_to_decimal(config: Config, pop_x, pop_y):
    max_index = binary_string_length(config.right_limit,
                                     config.left_limit,
                                     config.significant_figures) - 1
    return (config.left_limit + binary_to_decimal(list_to_string(pop_x)) * (config.right_limit - config.left_limit) / (
            2 ** max_index),
            config.left_limit + binary_to_decimal(list_to_string(pop_y)) * (config.right_limit - config.left_limit) / (
                    2 ** max_index))


def population_change_from_binary_to_decimal(config: Config, binary_population: Population):
    decimal_population = []
    for i in range(len(binary_population.individuals)):
        decimal_population.append(
            transform_binary_to_decimal(config, binary_population.individuals[i].chromosome.x,
                                        binary_population.individuals[i].chromosome.y))
    return decimal_population
