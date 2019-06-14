import random
import string
import numpy as np
from deap import algorithms, base, creator, tools

from objective.obj_fun import objective_fn_deap as objfn

"""
Creator is the class where we add attributes the GA
First one is the fitness function

for the fitness function the inherit class will be base.Fitness, the weights can be -1.0 for minization and 1.0 for maximization

@params
(Element alias, base class for that element, any other attr for that element)

https://deap.readthedocs.io/en/master/tutorials/basic/part1.html
"""
creator.create("FitnessMax", base.Fitness, weights=(1.0,))


"""
for the Individual (Input) we define its inherit class a simple python list and the fitness attribute to 
be the previously initialized one
"""
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
random.randint(0, 100)
"""
register is a function that takes two params first one is alias to the second param which is a function
any other params will be passed as the actual function parameter
EXAMPLE:
    toolbox.register("greeting", hello, string,5)
    def hello(y,x):
        for i in range(1,x):
            print(y)

As for the function initRepeat it calls the function container with a generator function
corresponding to the calling n times the function func.

https://deap.readthedocs.io/en/master/api/tools.html#deap.tools.initRepeat

@params
container   – The type to put in the data from func.
func        – The function that will be called n times to fill the container.
n           – The number of times to repeat func.
"""
toolbox.register("attr_bool", random.randint, 0, 100)
toolbox.register("attr_bool_char", random.choice, string.ascii_lowercase)


def CreateInd():
    result = creator.Individual(fitness=creator.FitnessMax)
    result.append(toolbox.attr_bool())
    result.append(toolbox.attr_bool())
    result.append(toolbox.attr_bool_char())
    return result

# IND_SIZE=3
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, IND_SIZE)
# toolbox.register("individual", tools.initRepeat, creator.Individual, CreateInd, 1)


"""
the upper two returns <class 'deap.creator.Individual'>
the first one assumes 3 int values from range (0:100) but the problem has a letter which is bound by the ascii limits
"""
toolbox.register("individual", CreateInd)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)


"""
now calling toolbox.individual() will return a complete creator.Individual r with a maximizing
single objective fitness attribute

and toolbox.population(n=) will generate random n individual 
"""

pop = toolbox.population(n=100)
# objfn(toolbox.individual())               //this is a test for the objfn and an individual to check

# cross over from one point only
toolbox.register("mate", tools.cxOnePoint)
# a kind of mutation that randomizes each gene within pre-defined limits and probability of the individual to be mutated
toolbox.register("mutate", tools.mutUniformInt, low=[0, 0, ord('a')], up=[100, 100, ord('z')], indpb=0.2)
# select size
toolbox.register("select", tools.selTournament, tournsize=10)
toolbox.register("evaluate", objfn)


# some variables for the verbose(log)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("max", np.max)

pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=50, stats=stats, verbose=True)
print(tools.selBest(pop, k=5))
