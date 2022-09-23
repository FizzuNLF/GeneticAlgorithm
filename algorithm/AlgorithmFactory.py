from enum import Enum

from algorithm.BestSelection import BestSelection
from algorithm.Roulette import Roulette
from algorithm.Tournament import Tournament
from utils.Config import Config


class SelectionMethod(Enum):
    Best = 'Best'
    Roulette = 'Roulette'
    Tournament = 'Tournament'


class SelectionFactory:
    config: Config = None

    def __init__(self, config: Config):
        self.config = config

    def create_alghoritm(self):
        selection_method = self.config.selection_method
        if selection_method == 'Best':
            return BestSelection(self.config)
        if selection_method == 'Roulette':
            return Roulette(self.config)
        if selection_method == 'Tournament':
            return Tournament(self.config)
