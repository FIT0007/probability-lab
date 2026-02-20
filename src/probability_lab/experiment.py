import random
from typing import List

def run_once():
    x = random.randint(1, 6)
    return x

##calculate the average of n trials, where if the first roll is 5, we roll 3 more times and add them to the total

def simulate(n: int):
    total_array = []
    for i in range (n):
        first = run_once()
        trial_total = 0
        if first == 5:
            trial_total = 0
            for j in range (3):
                trial_total+=run_once()
            total_array.append(trial_total+first)
        else:
            total_array.append(first)
    return total_array


