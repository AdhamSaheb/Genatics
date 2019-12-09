
class Solution:
    def __init__(self, list, groups, professors):
        self.list = list #12*5 = 60 slots
        self.groups = groups
        self.professors = professors
        self.chromosome = assemble(list)
        self.fitness = -1 #not assigned yet

    def __str__(self):
        return str(self.chromosome) + " " + str(self.list) + " " + str(self.fitness)

# assembling a 60 index list into a 12*6 chromosome
def assemble(list):
    chromosome = []
    i = 0
    while i < 60:
        sublist = []
        sublist.append(list[i])
        sublist.append(list[i + 1])
        sublist.append(list[i + 2])
        sublist.append(list[i + 3])
        sublist.append(list[i + 4])
        chromosome.append(sublist)
        i += 5
    return chromosome