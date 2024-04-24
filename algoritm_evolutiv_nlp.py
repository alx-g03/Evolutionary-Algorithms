import random
import math


def fitness(solution):
    return sum([-x * math.sin(math.sqrt(abs(x))) for x in solution])


def crossover(parent1, parent2):
    child = []
    for i in range(len(parent1)):
        if random.random() < 0.5:
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child


def mutate(solution):
    mutate_position = random.randint(0, len(solution) - 1)
    solution[mutate_position] = solution[mutate_position] + random.uniform(-0.1, 0.1)
    return solution


def selection(population, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        tournament = random.sample(population, 3)
        selected_parents.append(min(tournament, key=lambda x: fitness(x)))
    return selected_parents


def evolutionary_algorithm(n_dimensions, population_size, num_generations, num_parents, crossover_rate, mutation_rate):
    population = [[random.uniform(-500, 500) for _ in range(n_dimensions)] for _ in range(population_size)]
    for generation in range(num_generations):
        parents = selection(population, num_parents)
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = random.choices(parents, k=2)
            if random.random() < crossover_rate:
                child1 = crossover(parent1, parent2)
                child2 = crossover(parent2, parent1)
            else:
                child1 = parent1
                child2 = parent2
            if random.random() < mutation_rate:
                child1 = mutate(child1)
            if random.random() < mutation_rate:
                child2 = mutate(child2)
            new_population.append(child1)
            new_population.append(child2)
        population = new_population
        best_solution = min(population, key=lambda x: fitness(x))
        print(f"Generation {generation + 1}: Best solution = {best_solution}, Fitness = {fitness(best_solution)}")
    return min(population, key=lambda x: fitness(x)), fitness(min(population, key=lambda x: fitness(x)))
