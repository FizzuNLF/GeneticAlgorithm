import random
from copy import deepcopy

from FitnessFunction.FitnessFunction import function_booth_output
from models.Population import Population
from utils.Config import Config
import numpy as np


class Roulette:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def roulette_selection(self, binary_population: Population):
        roulette_list = []
        function_output_new = []
        function_output = function_booth_output(binary_population)
        for item in function_output:
            item = 1 / item
            function_output_new.append(item)

        sum_of_function_output = np.sum(function_output_new)
        for item in function_output_new:
            result = item / sum_of_function_output
            roulette_list.append(result)

        return roulette_list

    # obliczanie dystrybuanty
    def roulette_distribuation(self, roulette_list):
        x = 0
        roulette_result = []
        for i in range(len(roulette_list)):
            x += roulette_list[i]
            roulette_result.append(x)

        return roulette_result

    # zakręcenie kołem ruletki
    def roulette_spin(self, roulette_result):
        spin_result = random.random()
        roulette_index_result = None
        for item in roulette_result:
            x = item - spin_result
            if x < 0:
                continue
            else:
                roulette_index_result = roulette_result.index(item)
                break
        return roulette_index_result

    # przygotowanie indeksu kolejnej generacji
    def roulette_new_generation(self, binary_population: Population):
        roulette_list = self.roulette_selection(binary_population)
        roulette_result = self.roulette_distribuation(roulette_list)
        roulette_index_result = self.roulette_spin(roulette_result)

        return roulette_index_result

    # algorytmy genetyczny koła ruletki
    def calculate(self, binary_population: Population):
        new_population = deepcopy(binary_population)
        new_generation = []
        for i in range(self.config.number_of_population):
            new_generation.append(
                new_population.individuals[self.roulette_new_generation(new_population)])
        return Population(new_generation)
