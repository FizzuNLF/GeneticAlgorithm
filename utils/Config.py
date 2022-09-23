class Config:
    left_limit = -10
    right_limit = 10
    # dokładność do ilu liczb znaczących
    significant_figures = 2
    # ilość jednostek w populacji
    number_of_population = 10
    # liczba epok:
    number_of_eras = 20
    # selekcja najlepszych %
    selection_percent = 0.50
    # procent szans na krzyżowanie
    crossover_chance_percent = 0.80
    # procent szans na mutacje
    mutation_chance_percent = 0.25
    # procent szans na inwersję
    inversion_chance_percent = 0.10
    # elitarny procent
    elite_percent = 0.10
    # maximalization
    maximalization = False
    # wielkość grup turniejowych
    tournament_gourps_size = 3
    # algorytm
    type_of_algorithm = 'BEST'  # 'TOURNAMENT', 'ROULETTE'
    type_of_mutation = ''
    selection_method = None
    mutation_method = None
    cross_method = None

    def __init__(self, maximization=None, cross_method=None, mutation_method=None, selection_method=None,
                 left_limit=None,
                 right_limit=None, number_of_population=None, number_of_eras=None, crossover_percent=None,
                 mutation_percent=None, significant_figures=None, tournament_gourps_size=None, elite_percent=None,
                 selection_percent=None, inversion_chance_percent=None):
        self.maximalization = maximization
        self.mutation_chance_percent = mutation_percent
        self.selection_percent = selection_percent
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.number_of_population = number_of_population
        self.number_of_eras = number_of_eras
        self.crossover_chance_percent = crossover_percent
        self.significant_figures = significant_figures
        self.tournament_gourps_size = tournament_gourps_size
        self.elite_percent = elite_percent
        self.selection_method = selection_method
        self.mutation_method = mutation_method
        self.cross_method = cross_method
        self.inversion_chance_percent = inversion_chance_percent
