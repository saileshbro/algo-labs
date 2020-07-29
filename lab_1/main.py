from search import linear_search, binary_search
from random import sample, choice
from time import time
import csv
import matplotlib.pyplot as plt


def generateForLinear():
    linear_result = {
        "input_array": [],
        "exec_best": [],
        "exec_worst": [],
        "exec_avg": []
    }
    dataset = range(100000)
    for i in range(10, 100000, 250):
        data = sample(dataset, i)
        random = choice(data)
        linear_result["input_array"].append(i)
        start = time()
        linear_search(data, data[0])
        elapsed = time() - start
        linear_result["exec_best"].append(elapsed)
        start = time()
        linear_search(data, -10)
        elapsed = time() - start
        linear_result["exec_worst"].append(elapsed)

        start = time()
        linear_search(data, random)
        elapsed = time() - start
        linear_result["exec_avg"].append(elapsed)
    plt.figure(1, figsize=(14, 12))
    plt.title("Input size vs Exec time")
    plt.xlabel('Input size')
    plt.ylabel('Exec time')
    plt.plot(linear_result["input_array"],
             linear_result["exec_best"], c='green', label="Best case")
    plt.plot(linear_result["input_array"],
             linear_result["exec_worst"], c='red',  label="Worst case")
    plt.plot(linear_result["input_array"],
             linear_result["exec_avg"], c='blue',  label="Avg case")
    plt.legend()
    plt.show()


def generateForBinary():
    binary_result = {
        "input_array": [],
        "exec_best": [],
        "exec_worst": [],
        "exec_avg": [],
    }
    dataset = range(100000)
    for i in range(10, 100000, 250):
        data = sorted(sample(dataset, i))
        binary_result["input_array"].append(i)
        dataMiddle = data[(i-1)//2]
        start = time()
        # best case
        binary_search(data, dataMiddle, 0, i-1)
        elapsed = time() - start
        binary_result["exec_best"].append(elapsed)
        start = time()
        # worst case
        binary_search(data, 1, 0, i-1)
        elapsed = time() - start
        binary_result["exec_worst"].append(elapsed)
        random = choice(data)
        start = time()
        binary_search(data, random, 0, i-1)
        elapsed = time() - start
        binary_result["exec_avg"].append(elapsed)
    plt.figure(1, figsize=(14, 12))
    plt.title("Input size vs Exec time")
    plt.xlabel('Input size')
    plt.ylabel('Exec time')
    plt.plot(binary_result["input_array"],
             binary_result["exec_best"], c='green', label="Best case")
    plt.plot(binary_result["input_array"],
             binary_result["exec_worst"], c='red',  label="Worst case")
    plt.plot(binary_result["input_array"],
             binary_result["exec_avg"], c='blue',  label="Avg case")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    generateForBinary()
