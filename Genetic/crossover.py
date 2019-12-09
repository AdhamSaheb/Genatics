import random
from Models import *
import copy

from Models.Group import Group
from Models.Solution import Solution
from Genetic.Fitness import fitness_function


def breed_by_crossover(parent_1, parent_2, professors):
    # Get length of chromosome
    chromosome_length = len(parent_1.list)
    # Pick crossover point, avoding ends of chromsome
    crossover_points = random.sample(range(0, chromosome_length), 2)  # generate 2 random start and end points
    # performing ordered X1 crossover
    endpoint = 0
    start = 0
    if crossover_points[0] > crossover_points[1]:
        start = crossover_points[1]
        endpoint = crossover_points[0]
    else:
        start = crossover_points[0]
        endpoint = crossover_points[1]
    child_1 = []
    child_2 = []
    # initializing the new lists
    for i in range(chromosome_length):
        child_1.append(0)
        child_2.append(0)
    for i in range(start, endpoint):
        child_1[i] = parent_1.list[i]
        child_2[i] = parent_2.list[i]
    for i in range(0, start):
        child_1[i] = parent_2.list[i]
        child_2[i] = parent_1.list[i]
    for i in range(endpoint, chromosome_length):
        child_1[i] = parent_2.list[i]
        child_2[i] = parent_1.list[i]

    solution1 = list_to_sol(child_1, professors)

    solution2 = list_to_sol(child_2, professors)

    # Return solutions
    return solution1, solution2


# function used to mutate a chromosome
def mutate(solution, professors):
    newlist = copy.deepcopy(solution.list)
    listofobjects = []
    for i in range(len(newlist)):
        if isinstance(newlist[i], Group):
            listofobjects.append(i)

    index = random.sample(range(0, len(newlist)), 2)  # generate 2 random indexes to swap
    temp = newlist[index[0]]
    newlist[index[0]] = newlist[index[1]]
    newlist[index[1]] = temp
    new_solution = list_to_sol(newlist, professors)

    return new_solution


# converting a list to a solution
def list_to_sol(list1, professors):
    groups = []
    for group in list1:
        if isinstance(group,Group):
            groups.append(group)
    newprofessors = copy.deepcopy(professors)
    for professor in newprofessors:
        professor.numberofprojects = 0
    for group in groups:
        for professor in group.examinors:
            for professor1 in newprofessors:
                if professor.name == professor1.name:
                    professor1.numberofprojects += 1
    return Solution(list1, groups, newprofessors)


# re add professors
def breed_by_crossover2(parent_1, parent_2,professors):
    # Get length of chromosome
    chromosome_length = len(parent_1.list)
    # Pick crossover point, avoding ends of chromsome
    crossover_points = random.sample(range(0, chromosome_length), 2)  # generate 2 random start and end points
    # performing ordered X1 crossover
    endpoint = 0
    start = 0
    child1=copy.deepcopy(parent_1.list)
    child2=copy.deepcopy(parent_2.list)

    child3=copy.deepcopy(parent_2.list)
    child4=copy.deepcopy(parent_1.list)

    if crossover_points[0] > crossover_points[1]:
        start = crossover_points[1]
        endpoint = crossover_points[0]
    else:
        start = crossover_points[0]
        endpoint = crossover_points[1]

    length = endpoint - start
#First child
    for i in range(length):
        for entry2 in child2:
            if child1[i] == "Empty":
                if entry2=="Empty":
                    child2.remove(entry2)
                    break
            if isinstance(child1[i],Group):
                if isinstance(entry2,Group) and entry2.project==child1[i].project:
                    child2.remove(entry2)
                    break


    for i in range (length):
        child2.insert(start+i,child1[i])


#Second child
    for i in range(length):
        for entry2 in child4:
            if child3[i] == "Empty":
                if entry2 =="Empty":
                    child4.remove(entry2)
                    break
            if isinstance(child3[i], Group):
                if isinstance(entry2, Group) and entry2.project == child3[i].project:
                    child4.remove(entry2)
                    break

    for i in range(length):
        child4.insert(start + i, child3[i])

    solution1=list_to_sol(child2,professors)
    solution2=list_to_sol(child4,professors)
    solution1.fitness=fitness_function(solution1)
    solution2.fitness = fitness_function(solution2)
    return  solution1,solution2




def breed_by_crossover3(parent_1, parent_2,professors):
    # Get length of chromosome
    chromosome_length = len(parent_1.list)
    # Pick crossover point, avoding ends of chromsome
    # performing ordered X1 crossover
    endpoint = int(0.5*chromosome_length)
    start = 0
    child1=copy.deepcopy(parent_1.list)
    child2=copy.deepcopy(parent_2.list)

    child3=copy.deepcopy(parent_2.list)
    child4=copy.deepcopy(parent_1.list)


    length = endpoint - start
#First child
    for i in range(length):
        for entry2 in child2:
            if child1[i] == "Empty":
                if entry2=="Empty":
                    child2.remove(entry2)
                    break
            if isinstance(child1[i],Group):
                if isinstance(entry2,Group) and entry2.project==child1[i].project:
                    child2.remove(entry2)
                    break


    for i in range (length):
        child2.insert(start+i,child1[i])


#Second child
    for i in range(length):
        for entry2 in child4:
            if child3[i] == "Empty":
                if entry2 =="Empty":
                    child4.remove(entry2)
                    break
            if isinstance(child3[i], Group):
                if isinstance(entry2, Group) and entry2.project == child3[i].project:
                    child4.remove(entry2)
                    break

    for i in range(length):
        child4.insert(start + i, child3[i])

    solution1=list_to_sol(child2,professors)
    solution2=list_to_sol(child4,professors)
    solution1.fitness=fitness_function(solution1)
    solution2.fitness = fitness_function(solution2)
    return  solution1,solution2























