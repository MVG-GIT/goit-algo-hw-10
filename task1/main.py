import timeit
from greedy import find_coins_greedy
from dynamic import find_min_coins

coins = [50, 25, 10, 5, 2, 1]
amount = 113

results = {
    "Greedy":   timeit.timeit(lambda: find_coins_greedy(amount, coins), number=1000),
    "Dynamic":  timeit.timeit(lambda: find_min_coins(amount, coins), number=1000)
}

print("Execution time:")
for algo, t in results.items():
    print(f"{algo}: {t:.6f} s")


print("Results:")
print("Greedy:", find_coins_greedy(amount, coins))
print("Dynamic:", find_min_coins(amount, coins))
