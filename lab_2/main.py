from random import sample
from time import time_ns
from sorting import insertion_sort, merge_sort
import pandas as pd
import matplotlib.pyplot as plt


def generateForSorting():
    result = {
        "input_size": [],
        "exec_time_insertion": [],
        "exec_time_merge": [],
    }
    dataset = range(10000)
    for i in range(0, 10000, 10):
        data = sample(dataset, i)
        unsorted_copy = data.copy()
        result["input_size"].append(i)
        start = time_ns()
        insertion_sort(data)
        elapsed = time_ns()-start
        result["exec_time_insertion"].append(elapsed)
        start = time_ns()
        merge_sort(unsorted_copy, 0, len(unsorted_copy))
        elapsed_merge = time_ns()-start
        result["exec_time_merge"].append(elapsed_merge)
        print(f"{i},{elapsed},{elapsed_merge}")
    data_frame = pd.DataFrame.from_dict(result)
    data_frame.to_csv("sorting_data.csv", index=False)
    plt.figure(1, figsize=(14, 12))
    plt.title("Input size vs Exec time")
    plt.xlabel('Input size')
    plt.ylabel('Exec time')
    plt.plot(result["input_size"],
             result["exec_time_insertion"], c='green', label="Insertion Sort")
    plt.plot(result["input_size"],
             result["exec_time_merge"], c='blue',  label="Merge Sort")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    generateForSorting()
