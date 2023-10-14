import random
import numpy as np
# Define the size of the chessboard (8x8 for the 8-queens problem)
size = 8

def fitness_fn(board):
    # Calculate the fitness of an individual board (lower fitness is better)
    # Fitness is the number of attacking_pairs (queens attacking each other)
    attacking_pairs = 0
    for i in range(size):
        for j in range(i + 1, size):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacking_pairs += 1
    return attacking_pairs

def random_selection(population, fitness_fn):
    #Select a random individual from the population based on fitness
    weighted_population = [(ind, 1.0 / (fitness_fn(ind) + 1)) for ind in population]
    total_weight = sum(weight for ind, weight in weighted_population)
    rand_num = random.uniform(0, total_weight)
    cumulative_weight = 0
    for ind, weight in weighted_population:
        cumulative_weight += weight
        if cumulative_weight > rand_num:
            return ind

def reproduce(x, y):
    # Create a child by combining the genes of two parents (queens positions)
    n = len(x)
    crossover_point = random.randint(1, n - 1)
    child = x[:crossover_point] + y[crossover_point:]
    return child

def mutate(child):
    # Mutate a child by randomly changing the position of one queen
    index_to_mutate = random.randint(0, size - 1)
    new_position = random.randint(0, size - 1)
    child[index_to_mutate] = new_position
    return child

def genetic_algorithm(population, fitness_fn):
    n=0
    while True:
        new_population = []
        for i in range(len(population)):
            x = random_selection(population, fitness_fn)
            y = random_selection(population, fitness_fn)
            child = reproduce(x, y)
            if random.random() < 0.1:  # Small random probability for mutation
                child = mutate(child)
            new_population.append(child)
        population = new_population
        best_individual = min(population, key=fitness_fn)
        n=n+1
        if fitness_fn(best_individual) == 0:  # Solution found
            print(fitness_fn(best_individual))
            return best_individual
        elif n==200:
            print("Time-out!")
            print("Following is the best solution found --->")
            print(fitness_fn(best_individual))
            return best_individual

# Initialize the population with 100 random queen positions
initial_population = [[random.randint(0, size - 1) for i in range(size)] for j in range(100)]

# Solve the 8-queens problem using the genetic algorithm
solution = genetic_algorithm(initial_population, fitness_fn)
print("Solution:", solution)
state=[]
for i in range(8):
    row=[]
    row.extend([0,0,0,0,0,0,0,0])
    state.append(row)
    for k in range(8):
        if solution[k]==i:
            state[i][k]=1
for ele in state:
    print(ele)
