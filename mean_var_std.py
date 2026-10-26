import numpy as np


def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.array(lst).reshape(3, 3)

    stats = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    return {
        name: [
            func(arr, axis=0).tolist(),   # per column
            func(arr, axis=1).tolist(),   # per row
            func(arr.flatten()).item(),   # whole array
        ]
        for name, func in stats.items()
    }
