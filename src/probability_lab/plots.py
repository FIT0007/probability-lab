import matplotlib.pyplot as plt

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
    plt.title("Dice reroll: running mean")
    plt.xlabel("Trial number")
    plt.ylabel("Running mean")
    plt.plot(means, color="navy")
    plt.axhline(5.25, linestyle="--", color="crimson")
    plt.show()