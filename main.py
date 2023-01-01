import math
import pandas as pd
import matplotlib.pyplot as plt


def load_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def main():
    filename = "data.csv"
    df = load_csv(filename)

    # histogram
    plt.hist(df["Data"])
    plt.title("Гістограма")
    plt.show()

    minValue = math.floor(df["Data"].min())
    maxValue = math.ceil(df["Data"].max())

    # Frequency table
    freq_data = df.apply(pd.Series.value_counts, bins=[*range(minValue, maxValue + 1)])

    print()
    print("Frequency table")
    print()
    print(freq_data)

    # Statistics summary
    print()
    print("Statistics summary")
    print()
    print("Mean:", df["Data"].mean())
    print("Median:", df["Data"].median())
    print("Quantile:", df["Data"].quantile(0.75))


if __name__ == '__main__':
    main()
