# 1. Sample mean
# 2. Sample standard deviation
# 3. Median
# 4. A function that returns the n-quartil
# 5. A function that returns the n-percentil

import numpy as np


def mean(data):
    num_of_elements = len(data)
    sum_of_elements = sum(data)
    my_mean = sum_of_elements / num_of_elements
    return my_mean


def std_deviation(data):
    num_of_elements = len(data)
    sum_of_elements = sum(data)
    my_mean = sum_of_elements / num_of_elements
    variance = sum([((x - my_mean) ** 2) for x in data]) / num_of_elements
    stddev = variance ** 0.5
    return stddev


def median(data):
    if type(data) in [str]:
        raise TypeError("Input cannot be a string")
    num_of_elements = len(data)
    data.sort()
    if num_of_elements % 2 == 0:
        median1 = data[num_of_elements // 2]
        median2 = data[num_of_elements // 2 - 1]
        my_median = (median1 + median2) / 2
    else:
        my_median = data[num_of_elements // 2]
    return my_median


def quartil(data, n1, n2, n3):
    result1, result2, result3 = np.percentile(data, [n1, n2, n3])
    return result1, result2, result3


def percentil(data, n):
    result = np.percentile(data, n)
    return result
