from typing import List, Tuple

from FitnessFunction.FitnessFunction import function_booth
from utils.Config import Config


def find_best_result(result: List[Tuple[float, float]], config: Config):
    if len(result) == 0:
        return

    res = function_booth(result[0][0], result[0][1])
    best_tuple = result[0]
    for pair in result:
        function_output = function_booth(pair[0], pair[1])
        if not config.maximalization:
            if function_output < res:
                res = function_output
                best_tuple = pair
        else:
            if function_output > res:
                res = function_output
                best_tuple = pair

        return best_tuple, res
