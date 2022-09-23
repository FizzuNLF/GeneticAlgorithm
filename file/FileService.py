import pandas as pd
from pandas import DataFrame
import os.path


class FileService:
    file_name: str

    def __init__(self, file_name):
        self.file_name = file_name + '.csv'

    def add_row(self, epoch: int, best_value: float, mean: float, stdev: float):
        file_exists = os.path.exists(self.file_name)
        if file_exists:
            df = pd.DataFrame({"epoch": [epoch], 'best_value': [best_value], 'mean': [mean], 'stdev': [stdev]})
            df.to_csv(self.file_name, mode='a', header=False)
        else:
            df = pd.DataFrame({"epoch": [epoch], 'best_value': [best_value], 'mean': [mean], 'stdev': [stdev]})
            df.to_csv(self.file_name, mode='x')
