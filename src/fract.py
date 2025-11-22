import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def f(z):
    return np.square(z) - 1


z = [4, 1-0.2j, 1.6]
f(z)
