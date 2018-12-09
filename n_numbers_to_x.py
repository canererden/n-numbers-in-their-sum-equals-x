"""
gives n random value whose sum is equal to x
author: Caner Erden
"""
# %%
import numpy as np


def sum_to_x(n, x):
    values = [0.0, x] + list(np.random.uniform(low=0.0, high=x, size=n - 1))
    values.sort()
    return [values[i + 1] - values[i] for i in range(n)]
