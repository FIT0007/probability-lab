import random
from typing import List

import numpy
import matplotlib.pyplot as plt

def run_once():
    x = random.randint(1, 6)
    return x

def statistics(n: int):
    sum_results = 0
    for i in range (n):
        first = run_once()
        sum_results += first
        if first == 5:
            for j in range (3):
                second = run_once()
                sum_results += second
    print(f"Average: {sum_results/n}")

def main():
    print("Dice Rellor started")
    statistics(100000)

main()