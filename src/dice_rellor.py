import random
from typing import List
import matplotlib.pyplot as plt

import numpy
import matplotlib.pyplot as plt

def run_once():
    x = random.randint(1, 6)
    return x

##calculate the average of n trials, where if the first roll is 5, we roll 3 more times and add them to the total

def statistics(n: int):
    total_array = []
    trial_total = 0
    for i in range (n):
        first = run_once()
        if first == 5:
            trial_total = 0
            for j in range (3):
                trial_total+=run_once()
            total_array.append(trial_total+first)
        else:
            total_array.append(first)
    print(f"Average: {sum(total_array)/n}")
    print(len(total_array))
    return total_array

## plot a histogram of the results, with the x-axis being the result (sum per trial) and the y-axis being the frequency of that result. The histogram should have bins for each possible result (1-6 for the first roll, and 4-18 for the total if the first roll is 5). The histogram should also have a title and labels for the axes.

def plot_histogram(results):
    min_value = min(results)
    max_value = max(results)
    plt.figure()
    plt.hist(results, bins=range(min_value, max_value + 2), align="left")
    plt.title("Dice reroll: histogram")
    plt.xlabel("Result (sum per trial)")
    plt.ylabel("Frequency")
    plt.show()

## plot the running mean of the results, with the x-axis being the trial number and the y-axis being the running mean. The plot should have a title and labels for the axes.

def plot_running_mean(results):
    means = []
    running_sum = 0
    for i in range(len(results)):
        running_sum += results[i]
        means.append(running_sum / (i + 1))
    plt.figure()
    plt.plot(means)
    plt.title("Dice reroll: running mean")
    plt.xlabel("Trial number")
    plt.ylabel("Running mean")
    plt.show()

def main():
    print("Dice Reroll started")
    results = statistics(100000)
    plot_histogram(results)
    plot_running_mean(results)

if __name__ == "__main__":
    main()