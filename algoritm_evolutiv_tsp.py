import random
import math


def generate_random_solution(num_cities):
    cities = list(range(1, num_cities + 1))
    random.shuffle(cities)
    return cities


def calculate_distance(city1, city2):
    x1, y1 = city1[1], city1[2]
    x2, y2 = city2[1], city2[2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def tsp_fitness(solution, cities):
    total_distance = 0.0
    num_cities = len(solution)
    for i in range(num_cities):
        current_city = cities[solution[i] - 1]
        next_city = cities[solution[(i + 1) % num_cities] - 1]
        total_distance += calculate_distance(current_city, next_city)
    return total_distance


def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted([random.randint(0, size - 1) for _ in range(2)])
    child = [None] * size
    child[start:end] = parent1[start:end]
    remaining = [item for item in parent2 if item not in child]
    pos = 0
    for i in range(size):
        if None in child:
            if child[i] is None:
                while remaining[pos] in child:
                    pos += 1
                child[i] = remaining[pos]
                pos += 1
    return child


def mutate(solution):
    size = len(solution)
    idx1, idx2 = random.sample(range(size), 2)
    solution[idx1], solution[idx2] = solution[idx2], solution[idx1]
    return solution


def evolutionary_algorithm_tsp(cities, population_size, num_generations, crossover_prob, mutation_prob):
    population = [generate_random_solution(len(cities)) for _ in range(population_size)]

    for generation in range(num_generations):
        offspring = []
        for _ in range(population_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            if random.random() < crossover_prob:
                child1 = crossover(parent1, parent2)
                child2 = crossover(parent2, parent1)
            else:
                child1 = parent1[:]
                child2 = parent2[:]
            if random.random() < mutation_prob:
                child1 = mutate(child1)
            if random.random() < mutation_prob:
                child2 = mutate(child2)
            offspring.append(child1)
            offspring.append(child2)

        population += offspring

        population = sorted(population, key=lambda x: tsp_fitness(x, cities))[:population_size]

        best_solution = population[0]
        best_fitness = tsp_fitness(best_solution, cities)
        print(f"Generatia {generation + 1}: Cel mai bun individ: {best_solution}, Fitness: {best_fitness}")
