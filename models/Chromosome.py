import random
from utils.Config import Config


class Chromosome:
    x: float = 0
    y: float = 0

    def __init__(self, config: Config):
        if config is None:
            self.x = 0
            self.y = 0
            return
        self.x = random.uniform(config.right_limit, config.left_limit)
        self.y = random.uniform(config.right_limit, config.left_limit)

    @staticmethod
    def from_tuple(tuple: [float, float]):
        chrom = Chromosome(None)
        chrom.x = tuple[0]
        chrom.y = tuple[1]
        return chrom
