from FitnessFunction.FitnessFunction import function_booth_output
from crossover.ArytmeticCrossover import ArithmeticCrossover
from crossover.HeuristicCrossover import HeuristicCrossover
from models.Population import Population
from mutations.GaussMutation import GaussMutation
from mutations.UniformMutation import UniformMutation
from utils.Config import Config

config = Config(right_limit=-10, left_limit=10, number_of_population=4, elite_percent=0.4, crossover_percent=0.5,
                mutation_percent=1)

population = Population.initialize_random(4, config)

crossover = HeuristicCrossover(config)

next_gen = crossover.crossover(population)

mutation = GaussMutation(config)
mutated = mutation.mutate(population)

output = function_booth_output(mutated)

print()
