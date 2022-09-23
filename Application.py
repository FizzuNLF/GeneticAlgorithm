from FitnessFunction.FitnessFunction import function_booth, function_booth_output
from algorithm.AlgorithmFactory import SelectionFactory
from crossover.CrossoverFactory import CrossoverFactory
from file.FileService import FileService
from models.Population import Population
from mutations.Inversion import Inversion
from utils.Config import Config
from mutations.MutationFactory import MutationFactory
from utils.elite_strategy import elite_strategy
from utils.find_best_result import find_best_result
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Application:

    def __init__(self, config: Config):
        self.config = config

    def run(self):
        population: Population = Population(self.config).initialize_random(
            individuals_number=self.config.number_of_population,
            config=self.config
        )

        selection_method = SelectionFactory(config=self.config).create_alghoritm()
        crossover = CrossoverFactory(config=self.config).create_crossover()
        mutation = MutationFactory(config=self.config).create_mutation_algorithm()

        fs = FileService('results')

        for epoch in range(self.config.number_of_eras):
            best = elite_strategy(population, self.config)
            selected = selection_method.calculate(population)
            crossovered = crossover.crossover(selected)
            mutated = mutation.mutate(crossovered)
            population = Population(best.individuals + mutated.individuals)

            results = function_booth_output(population)
            tmp = list(map(lambda ind: (ind.chromosome.x, ind.chromosome.y), population.individuals))
            _, best = find_best_result(tmp, self.config)
            print(find_best_result(tmp, self.config))
            mean = np.mean(results)
            stdev = np.std(results)
            fs.add_row(epoch, best, mean, stdev)

        tmp = list(map(lambda ind: (ind.chromosome.x, ind.chromosome.y), population.individuals))
        self.generate_charts()
        return find_best_result(tmp, self.config)

    def generate_charts(self):
        df = pd.read_csv('results.csv')
        epoch = df['epoch']
        plt.plot(epoch, df['best_value'])
        plt.xlabel('epoch')
        plt.ylabel('best value')
        plt.title('Best value')
        plt.savefig('best', )

        plt.plot(epoch, df['mean'])
        plt.ylabel('mean')
        plt.title('Mean')
        plt.savefig('mean')

        plt.plot(epoch, df['stdev'])
        plt.ylabel('std')
        plt.title('standard deviation')
        plt.savefig('stdev')
