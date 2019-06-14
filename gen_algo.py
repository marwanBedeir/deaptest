import string

import itertools

import numpy as np

import random

import sys


#Generational GA
#Random Resetting
#Random Resetting is an extension of the bit flip for the integer representation
# .In this, a random value from the set of permissible values is assigned
# to a randomly chosen gene.
def mutate(parents,k):
    mutated = []
    n = int(len(parents))
    children = [random.choice(parents) for i in range(k)]

    for result,a,b,c in children:
        rand = np.random.randint(1, 3)
        if rand == 1:
            letter = string.ascii_lowercase
            char = random.choice(letter)
        elif rand == 2:
            a = np.random.randint(0, 100)
            letter = string.ascii_lowercase
            char = random.choice(letter)
        elif rand == 3:
            b = np.random.randint(0, 100)
            letter = string.ascii_lowercase
            char = random.choice(letter)
        mutated.append((result,a,b,char))
    return mutated
#One Point Crossover
def crossover(par_1,par_2):

    par_1 = list(par_1)
    par_2 = list(par_2)
    size = min(len(par_1),len(par_2))
    cxpoint = random.randint(1, size - 1)

    par_1[cxpoint:], par_2[cxpoint:] = par_2[cxpoint:], par_1[cxpoint:]

    return [(par_1[0],par_1[1],par_1[2],par_1[3]),(par_2[0],par_2[1],par_2[2],par_2[3])]

def evaluate_fitness(paranets,objfunction):
    evaluated_parents = []
    for result,a,b,c in paranets:
        x = objfunction(a,b,c)
        zipped = (x,a,b,c)
        evaluated_parents.append(zipped)
    return evaluated_parents

def Select_random(parents,k):
    selected =[random.choice(parents) for i in range(k)]
    return selected

def Tournament_Selection(parents,tournsize,k):
    best = []
    for i in range(k):
        selected = Select_random(parents,tournsize)
        mx = -10000000000
        for result,a,b,c in selected:
                if (mx < objective_fn(a, b, c)):
                    mx = objective_fn(a, b, c)
                    ma = a
                    mb = b
                    mc = c

        best.append((mx,ma,mb,mc))
    return best

def initialize_population(start,end,pop_size=10):
    init_pop_x = list(np.random.randint(start,end,size=pop_size))
    init_pop_y = list(np.random.randint(start,end,size=pop_size))
    letter = string.ascii_lowercase
    init_pop_char= [random.choice(letter) for i in range(start,end)]
    zeros = [ 0 for i in range(start,end)]
    init_pop = list(zip(zeros,init_pop_x,init_pop_y,init_pop_char))
    return init_pop

def GA(population,fitness_function,max_gen=100,pop_size=100,ratio = 5,tournsize=5):
    history = []
    all_pop = population
    for i in range(max_gen):
        all_pop = evaluate_fitness(all_pop,fitness_function)

        best_parents = Tournament_Selection(all_pop, tournsize, int((ratio / 100) * pop_size))

        all_pop.sort(reverse=True)

        all_pop = all_pop[:len(all_pop) - int((ratio/100)*pop_size)]

        all_pop = all_pop+best_parents

        all_pop.sort(reverse=True)

        crossed_over = crossover(all_pop[0],all_pop[1])

        all_pop = all_pop[:len(all_pop) - int((ratio / 100) * pop_size)]

        all_pop+=crossed_over

        all_pop.sort(reverse = True)

        mutated = mutate(all_pop,tournsize)

        all_pop.sort(reverse=True)

        all_pop = all_pop[:len(all_pop) - int((ratio/100)*pop_size)]

        all_pop+=mutated

        all_pop.sort(reverse=True)


    return all_pop









#---------------------------------------------------------------------------------------------------#

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

    v1_rnd = 20 #np.sum(-np.abs(v1 - np.random.randint(50, 80, [5, ])))

    v2_rnd = 10 #np.sum(-np.abs(v1 - np.random.randint(15, 54, [5, ])))

    v3 = ord(v3)

    return -(v1 + v2 - v3) ** 2 + v1_rnd + v2_rnd







pop = initialize_population(1,100,100)
#print(list(pop))
result = GA(pop,objective_fn,max_gen=100,pop_size=100,ratio=5,tournsize=10)
print(result)

a_list = list(range(100))

b_list = list(range(100))

c_list = [c for c in string.ascii_lowercase]

# brute-force solution

inputs = list(itertools.product(a_list, b_list, c_list))

outputs = np.array([objective_fn(a, b, c) for a, b, c in inputs])

sort_indices = np.argsort(outputs)[::-1]

sorted_outputs = outputs[sort_indices]

sorted_inputs = np.array(inputs)[sort_indices]

best_solution = sorted_inputs[0]

print("Best solution: %s" % best_solution,sorted_outputs[0])
