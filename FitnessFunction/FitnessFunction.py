from models.Population import Population
from utils.Config import Config
from utils.transform_binary_to_decimal import population_change_from_binary_to_decimal


def function_booth(zmienne_x, zmienna_y):
    return (zmienne_x + 2 * zmienna_y - 7) ** 2 + (2 * zmienne_x + zmienna_y - 5) ** 2


def function_booth_output(decimal_population: Population):
    output = []
    for i in range(len(decimal_population.individuals)):
        output.append(function_booth(decimal_population.individuals[i].chromosome.x,
                                     decimal_population.individuals[i].chromosome.y))
    return output
