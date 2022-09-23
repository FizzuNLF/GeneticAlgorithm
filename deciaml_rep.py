import random
from copy import deepcopy
import statistics

left_limit = -10
right_limit = 10
number_of_population = 10
crossover_chance_percent = 0.8
mutation_chance_percent = 0.3
elite_percent = 0.5


# Booth function f(x,y) = 0 dla x = 1, y = 3
def function_booth(zmienne_x, zmienna_y):
    return (zmienne_x + 2 * zmienna_y - 7) ** 2 + (2 * zmienne_x + zmienna_y - 5) ** 2


# generacja populacji
def generate_population():
    decimal_population = []
    for i in range(2):
        decimal_population.append([random.uniform(left_limit, right_limit) for y in range(number_of_population)])

    return list(zip(decimal_population[0], decimal_population[1]))


# krzyżowanie arytmetyczne
def arytmetic_crossover(decimal_population):
    next_generation = []
    current_generation = deepcopy(decimal_population)
    while len(next_generation) < number_of_population - number_of_population * elite_percent:
        index_no_1 = random.randint(0, len(current_generation) - 1)
        index_no_2 = random.randint(0, len(current_generation) - 1)
        crossover_probability = random.random()
        if crossover_probability <= crossover_chance_percent and index_no_1 != index_no_2:
            k_parameter = random.random()
            new = [(
                k_parameter * current_generation[index_no_1][0] + (1 - k_parameter) * current_generation[index_no_2][0],
                k_parameter * current_generation[index_no_1][1] + (1 - k_parameter) * current_generation[index_no_2][1])
                , (
                    (1 - k_parameter) * current_generation[index_no_1][0] + k_parameter *
                    current_generation[index_no_2][0],
                    (1 - k_parameter) * current_generation[index_no_1][1] + k_parameter *
                    current_generation[index_no_2][1])
            ]
            if len(next_generation) <= number_of_population - number_of_population * elite_percent - 2:
                next_generation.append(new[0])
                next_generation.append(new[1])
            elif len(next_generation) <= number_of_population - number_of_population * elite_percent - 1:
                next_generation.append(new[0])

    return next_generation


# krzyżowanie heurystyczne
def heuristic_crossover(decimal_population):
    next_generation = []
    while len(next_generation) < number_of_population - number_of_population * elite_percent:
        current_generation = deepcopy(decimal_population)
        index_no_1 = random.randint(0, len(current_generation) - 1)
        index_no_2 = random.randint(0, len(current_generation) - 1)
        crossover_probability = random.random()
        k_parameter = random.random()
        if crossover_probability <= crossover_chance_percent and current_generation[index_no_1][0] > \
                current_generation[index_no_2][0] and current_generation[index_no_1][1] > \
                current_generation[index_no_2][1]:
            next_generation.append((k_parameter * (
                    current_generation[index_no_1][0] - current_generation[index_no_2][0]) +
                                    current_generation[index_no_2][0], k_parameter * (
                                            current_generation[index_no_1][1] - current_generation[index_no_2][1]) +
                                    current_generation[index_no_2][1]))
        elif crossover_probability <= crossover_chance_percent and current_generation[index_no_1][0] < \
                current_generation[index_no_2][0] and current_generation[index_no_1][1] < \
                current_generation[index_no_2][1]:
            next_generation.append((k_parameter * (
                    current_generation[index_no_2][0] - current_generation[index_no_1][0]) +
                                    current_generation[index_no_1][0], k_parameter * (
                                            current_generation[index_no_2][1] - current_generation[index_no_1][1]) +
                                    current_generation[index_no_1][1]))

    return next_generation


# mutacja równomierna
def uniform_mutation(decimal_population):
    next_generation = []
    current_generation = deepcopy(decimal_population)
    for i in range(len(current_generation)):
        mutation_probability = random.random()
        if mutation_probability <= mutation_chance_percent:
            mutation_index = random.randint(0, 1)
            if mutation_index == 0:
                next_generation.append((random.uniform(-10, 10), current_generation[i][1]))
            elif mutation_index == 1:
                next_generation.append((current_generation[i][0], random.uniform(left_limit, right_limit)))
        else:
            next_generation.append(current_generation[i])

    return next_generation


# obliczanie średnich ze zbioru
def mean_calculation(decimal_population):
    current_generation = deepcopy(decimal_population)
    x = []
    y = []
    for i in range(len(decimal_population)):
        x.append(current_generation[i][0])
        y.append(current_generation[i][1])

    return statistics.mean(x), statistics.mean(y)


# obliczanie średnich ze zbioru
def std_calculation(decimal_population):
    current_generation = deepcopy(decimal_population)
    x = []
    y = []
    for i in range(len(decimal_population)):
        x.append(current_generation[i][0])
        y.append(current_generation[i][1])

    return statistics.stdev(x), statistics.stdev(y)


# mutacja gaussa
def gauss_mutation(decimal_population):
    next_generation = []
    current_generation = deepcopy(decimal_population)
    x_mean, y_mean = mean_calculation(current_generation)
    x_std, y_std = std_calculation(current_generation)
    for i in range(len(current_generation)):
        mutation_probability = random.random()
        if mutation_probability <= mutation_chance_percent:
            new = (current_generation[i][0]+random.gauss(x_mean, x_std), current_generation[i][1]+random.gauss(y_mean, y_std))
            if left_limit <= new[0] <= right_limit and left_limit <= new[1] <= right_limit:
                next_generation.append(new)
            else:
                next_generation.append(current_generation[i])
        else:
            next_generation.append(current_generation[i])

    return next_generation


population = generate_population()
print('population: ', population)
print('arytmetic:  ', arytmetic_crossover(population))
print('heuristic:  ', heuristic_crossover(population))
print('uni muta:   ', uniform_mutation(population))
print('gauss muta: ', gauss_mutation(population))
