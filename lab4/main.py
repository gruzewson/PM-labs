import random
from tabulate import tabulate

def main():
    n = 100000

    X = [1, 2, 3, 4]
    F_X = [0.5, 0.7, 0.9, 1]
    F_Y = [[0.2, 0.2, 0.2, 1],
           [1, 1, 1, 1],
           [0, 0.5, 0.5, 1],
           [0, 0, 1, 1]]

    x_temp = 0
    y_temp = 0

    results = [[0 for _ in range(4)] for _ in range(4)]

    for _ in range(n):
        y = random.random()
        for j in range(4):
            if y < F_X[j]:
                x_temp = X[j]
                F = F_Y[j]

                y2 = random.random()
                for i in range(4):
                    if y2 < F[i]:
                        y_temp = X[i]
                        break
                break
        results[x_temp - 1][y_temp - 1] += 1

    print(tabulate(results, tablefmt='psql', colalign=('center', 'center')))

main()
