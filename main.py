import matplotlib.pyplot as plt
import numpy as np
import scipy as sc


def main():
    Var = 16
    loc = Var
    scale = Var / 10
    size = Var * 100
    np.random.seed(1)

    dataset = np.random.normal(loc, scale, size)
    counts, bins, bars = plt.hist(dataset)
    dataset_freq = [*map(lambda x: x / size, counts)]

    plt.title("Гістограма для вибірки")
    plt.show()

    chi_square_res = sc.stats.chisquare(dataset_freq)

    print(chi_square_res)
    # The chi-squared statistic is a single number that tells you how much difference
    # exists between your observed counts and the counts you would expect if there were no relationship at all
    # in the population.

    # Small p-values (under 5%) usually indicate that a difference is significant
    # (or “small enough”).
    # P values are expressed as decimals although it may be easier to understand what they are if you convert them
    # to a percentage. For example, a p value of 0.0254 is 2.54%. This means there is a 2.54% chance your results
    # could be random (i.e. happened by chance). That’s pretty tiny. On the other hand, a large p-value of .9(90%)
    # means your results have a 90% probability of being completely random and not due to anything in your experiment.

    dataset_m = (dataset - loc) / scale
    ks_res = sc.stats.kstest(dataset_m, "norm")
    print(ks_res)
    # всі ці тести допомагають дізнатися наскільки експеремент був незалежним (рандомним), а отже це свідчить
    # про його об'єктивність і правильність


if __name__ == '__main__':
    main()
