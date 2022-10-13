import array
import random

from deap import base
from deap import creator
from deap import tools

#Fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("FitnessMulti", base.Fitness, weights=(-1.0, 1.0))

def List_of_Floats():
    creator.create("Individual", list, fitness=creator.FitnessMin)
    IND_SIZE=10
    toolbox = base.Toolbox()
    toolbox.register("attr_float",random.random)
    toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_float,n=IND_SIZE)
    return toolbox

def Permutation():
    creator.create("Individual",list,fitness=creator.FitnessMin)
    IND_SIZE = 10
    toolbox = base.Toolbox()
    toolbox.register("indices",random.sample,range(IND_SIZE),IND_SIZE)
    toolbox.register("individual",tools.initIterate,creator.Individual,toolbox.indices)
    return toolbox

def Arithmetic_Expression():
    



if __name__ == '__main__':
    toolbox = List_of_Floats()
    ind = toolbox.individual()
    toolbox = Permutation()
    ind = toolbox.individual()
    pass