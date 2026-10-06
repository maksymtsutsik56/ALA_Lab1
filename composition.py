import numpy as np
from viz import plot_shape


def apply_sequence(X, steps):
    current = X
    total = np.eye(2) 

    for name, func, params in steps:
        current, A = func(current, *params)
        total = A @ total  
        plot_shape(X, current, A, name)

    order = " → ".join(name for name, _, _ in steps)
    plot_shape(X, current, total, f"Total: {order}")
    return current, total