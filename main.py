import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def main():
    Var = 16
    loc = Var
    scale = Var / 10
    size = Var * 100
    dataset = np.random.normal(loc, scale, size)
    print(len(dataset))


if __name__ == '__main__':
    main()
