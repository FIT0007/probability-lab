from probability_lab.experiment import simulate
from probability_lab.stats import mean, variance
from probability_lab.plots import plot_histogram, plot_running_mean
import argparse


def main():
    parser = argparse.ArgumentParser(description="Dice reroll simulation")
    parser.add_argument("--trials", type=int, default=100000,
                    help="Number of simulation trials")
    parser.add_argument("--no-plots", action="store_true",
                    help="Disable plots")
    args = parser.parse_args()

    results = simulate(args.trials)
    mu = mean(results)
    var = variance(results, mu)

    print("Mean:", mu)
    print("Variance:", var)

    plot_histogram(results)
    plot_running_mean(results)

    if not args.no_plots:
        plot_histogram(results)
        plot_running_mean(results)

    ##print("min/max:", min(results), max(results))


if __name__ == "__main__":
    main()
