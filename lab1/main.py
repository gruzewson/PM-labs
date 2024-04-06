import math

def getdata(file_name):
    data = []
    number_of_lines = 15

    with open(file_name, 'r') as file:
        file.readline()
        for _ in range(number_of_lines):
            line = file.readline().strip().split(' ')
            id, town, population, latitude, longitude = line
            data.append((int(id), town, int(population), float(latitude), float(longitude)))

    return data

def backtrack(path, nums, counter, K, combinations):
    if len(path) == K:
        print(f"{counter[0]}: {path}")
        combinations.append(path.copy())
        counter[0] += 1
        return
    for num in nums:
        if num not in path:
            path.append(num)
            backtrack(path, nums, counter, K, combinations)
            path.pop()

def generate_combinations(N, K):
    counter = [1]
    nums = list(range(1, N + 1))
    combinations = []
    backtrack([], nums, counter, K, combinations)
    return combinations

def is_repeated(combinations, path):
    for comb in combinations:
        if sorted(comb) == sorted(path):
            return True
    return False

def backtrack_rep(path, nums, counter, K, combinations):
    if len(path) == K:
        if is_repeated(combinations, path) == False:
            print(f"{counter[0]}: {path}")
            combinations.append(path.copy())
            counter[0] += 1
        return
    for num in nums:
        path.append(num)
        backtrack_rep(path, nums, counter, K, combinations)
        path.pop()

def generate_with_rep(N, K):
    counter = [1]
    nums = list(range(1, N + 1))
    combinations = []
    backtrack_rep([], nums, counter, K, combinations)


data = getdata("italy.in")
#1
N = 4
K = 3
print("1.\n")
combinations = generate_combinations(N, K)
cities_comb = []

for comb in combinations:
    path = []
    for index in comb:
        city = data[index - 1]
        path.append(city)
    cities_comb.append(path)

#1d
shortest_dist = math.inf
for comb in cities_comb:
    dist = 0
    for i in range(1, len(comb)):
        x1 = comb[i][3]
        x2 = comb[i - 1][3]
        y1 = comb[i][4]
        y2 = comb[i - 1][4]
        dist += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dist < shortest_dist:
        shortest_dist = dist
        best_comb = comb

print("\n1d.")
print("Shortest path: ", shortest_dist)
cities_names = []
for city in best_comb:
    cities_names.append(city[1])

cities_string = ', '.join(cities_names)
print(f"path: {cities_string}")

#2d
biggest_avg_pop = -math.inf
for comb in cities_comb:
    population = 0
    for i in range(len(comb)):
        population += comb[i][2]
    if population/len(comb) > biggest_avg_pop:
        biggest_avg_pop = population/len(comb)
        best_comb = comb

print("\n2d.")
print("Biggest avg population: ", biggest_avg_pop)
cities_names = []
for city in best_comb:
    cities_names.append(city[1])

cities_string = ', '.join(cities_names)
print(f"cities: {cities_string}")