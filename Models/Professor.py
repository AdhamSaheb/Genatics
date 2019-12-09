import  random

class Professor:

    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        self.numberofprojects = 0

    def __str__(self):
        return "Name: " + self.name + ", Subjects=" + str(self.subjects) + ", Number of projects: " + str(
            self.numberofprojects)


# validdoctors method will return a list of all possible valid examinors
def validdoctors(group, professors):
    professor_list = []
    for professor in professors:
        if professor.name == group.supervisor:
            continue
        else:
            if common_data(group.subjects, professor.subjects):
                professor_list.append(professor)
    while len(professor_list)<2:
        index = random.randint(1,len(professors)-1)
        if (professors[index].name == group.supervisor):
            continue
        else:
            professor_list.append(professors[index])

        '''for i in professor_list:
        print(str(i)+ "For group" + str(group.project))'''
    return professor_list


# This function checks if there is common data between 2 lists
def common_data(list1, list2):
    # this is a functions that checks if 2 lists have at least one element in common
    result = False

    # traverse in the 1st list
    for x in list1:

        # traverse in the 2nd list
        for y in list2:

            # if one common
            if x == y:
                result = True
                return result

    return result
