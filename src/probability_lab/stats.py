
def mean(results):
    return sum(results) / len(results)

def variance(results, mu):
    return sum((x - mu) ** 2 for x in results) / len(results)