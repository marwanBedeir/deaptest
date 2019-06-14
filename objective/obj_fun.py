import numpy as np

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
    v1_rnd = np.sum(-np.abs(v1 - np.random.randint(50, 80, [5, ])))
    v2_rnd = np.sum(-np.abs(v1 - np.random.randint(15, 54, [5, ])))

    v3 = ord(v3)
    return -(v1 + v2 - v3) ** 2 + v1_rnd + v2_rnd


def objective_fn_deap(ind):
    v1, v2, v3 = ind[0], ind[1], ind[2]

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
    v1_rnd = np.sum(-np.abs(v1 - np.random.randint(50, 80, [5, ])))
    v2_rnd = np.sum(-np.abs(v1 - np.random.randint(15, 54, [5, ])))
    if isinstance(v3, str):
        v3 = ord(v3)
    else:
        v3 = v3

    return -(v1 + v2 - v3) ** 2 + v1_rnd + v2_rnd,
    #it returns tuple as DEAP requires the eval function to return that
