import math


# obliczanie jak długi ma być kod genetyczny
def binary_string_length(right_limit: float, left_limit: float, significant_figures: int):
    return math.ceil(math.log((right_limit - left_limit) * 10 ** significant_figures, 2) + math.log(1, 2))
