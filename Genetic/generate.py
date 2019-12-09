import copy
import random
from Models.Professor import validdoctors
from Models.Solution import Solution


def generate(groups, professors):
    newgroups = copy.deepcopy(groups)
    newprofessors = copy.deepcopy(professors)
    for group in newgroups:
        group.validexaminors = validdoctors(group, newprofessors)
    assign(newgroups, newprofessors)

    list = []

    for i in range(0, 60):
        list.append("Empty")  # initializing the list

    index = random.sample(range(0, 60), len(newgroups))  # generate random spots for groups inside the list
    i = 0
    for group in newgroups:  # assigning every group to a random spot
        list[index[i]] = group
        i += 1
    final = Solution(list, newgroups, newprofessors)

    return final

def assign(groups, professors):

    for group in groups:
        group.validexaminors.sort(key=lambda x: x.numberofprojects,reverse = False)
        index = [0,1]  # generate 2 random indexes for valid doctors

        for professor in professors:

            if group.validexaminors[index[0]].name == professor.name :
                if professor.numberofprojects>=6:
                    professors.sort(key=lambda x: x.numberofprojects,reverse = False)
                    candidate=professors[0]

                    if(candidate.name==group.supervisor):
                        candidate=professors[1]
                    group.examinors.append(candidate)
                    candidate.numberofprojects+=1
                else:
                    group.examinors.append(professor)
                    professor.numberofprojects+=1


            if group.validexaminors[index[1]].name == professor.name :
                if professor.numberofprojects>=6:
                    professors.sort(key=lambda x: x.numberofprojects,reverse = False)
                    candidate=professors[0]
                    if(candidate.name==group.supervisor):
                        candidate=professors[1]
                    group.examinors.append(candidate)
                    candidate.numberofprojects+=1
                else:
                    group.examinors.append(professor)
                    professor.numberofprojects+=1



