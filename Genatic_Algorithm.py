import numpy as np
import string
import random as rn
import sys


def genetic_alg(pop, objective, gen_size=100, pop_size=100, ratio=5, fittest_size=5):
    all_pop = pop
    for i in range(gen_size):
        all_pop = calc_fitness(all_pop, objective)
        fittest = calc_fittest(all_pop, fittest_size, int((ratio / 100) * pop_size))
        all_pop.sort(reverse=True)

        all_pop = all_pop[:len(all_pop) - int((ratio / 100) * pop_size)]
        all_pop += fittest
        all_pop.sort(reverse=True)

        children = cross_over(all_pop[0], all_pop[1])
        all_pop += children
        all_pop.sort(reverse=True)

        mutants = mutant(all_pop, fittest_size)
        all_pop += mutants
        all_pop.sort(reverse=True)

    return all_pop


def calc_fittest(parents, fittest_size, ratio):
    best = []
    for i in range(ratio):
        selected = [rn.choice(parents) for i in range(fittest_size)]
        mx = -sys.maxsize
        for _, a, b, c in selected:
            res = objective_fn(a, b, c)
            if res >= mx:
                mx = res
                global na, nb, nc
                na = a
                nb = b
                nc = c

        best.append((mx, na, nb, nc))

        return best


def mutant(parents, mutation_prop):
    mutated = []
    children = [rn.choice(parents) for i in range(mutation_prop)]

    for _, a, b, c in children:
        rand = np.random.randint(1, 3)
        if rand == 1:
            letter = string.ascii_lowercase
            char = rn.choice(letter)
        elif rand == 2:
            a = np.random.randint(0, 100)
            letter = string.ascii_lowercase
            char = rn.choice(letter)
        elif rand == 3:
            b = np.random.randint(0, 100)
            letter = string.ascii_lowercase
            char = rn.choice(letter)
        mutated.append((_, a, b, char))

    return mutated


def cross_over(parent_1, parent_2):
    parent_1 = list(parent_1)
    parent_2 = list(parent_2)
    n = len(min(parent_1,parent_2))
    crossover_point = rn.randint(1, n - 1)
    parent_1[crossover_point:], parent_2[crossover_point:] = parent_2[crossover_point:], parent_1[crossover_point:]
    return [tuple(parent_1), tuple(parent_2)]


def population(start, end, popsize=10):
    individual1 = list(np.random.randint(start, end, size=popsize))
    individual2 = list(np.random.randint(start, end, size=popsize))
    individual3 = [rn.choice(string.ascii_lowercase) for i in range(start, end)]
    zeros = [0 for i in range(start, end)]
    return list(zip(zeros, individual1, individual2, individual3))


def calc_fitness(parents, obj_function):
    fitness = []
    for _, a, b, c in parents:
        x = obj_function(a, b, c)
        y = (x, a, b, c)
        fitness.append(y)

    return fitness


def objective_fn(v1, v2, v3):
    """ Sample objective function for evolutionary algorithm



    :param v1: int

        int value of param 1

    :param v2: int

        int value of param 2

    :param v3: character

        char value of param 3



    :return:

    float : objective value



    """

    v1_rnd = 20  # np.sum(-np.abs(v1 - np.random.randint(50, 80, [5, ])))

    v2_rnd = 10  # np.sum(-np.abs(v1 - np.random.randint(15, 54, [5, ])))

    v3 = ord(v3)

    return -(v1 + v2 - v3) ** 2 + v1_rnd + v2_rnd


pop = population(1, 100, 100)
result = genetic_alg(pop, objective_fn, gen_size=100, pop_size=100, ratio=5, fittest_size=10)
result.sort(reverse=True)
print(result[0])
