from Models.Group import Group


def fitness_function(solution):
    if hard_fitness(solution):
        return 1 + soft_fitness(solution)
    else:
        return 0


# Function To Check Hard Constraints
def hard_fitness(solution):
    professors = solution.professors
    chromosome = solution.chromosome
    # takes 12x5 chromosome
    # Check that each professor has between 3 and 6 projects to examine
    for professor in professors:
        if professor.numberofprojects > 6:  # there is no < 3 now
            return False

    # Check if an examiner has 2 projects at the same time -> Hard Constraint #2
    for gene in chromosome:
        for i in range(0, 5):
            for j in range(i + 1, 5):
                if gene[i] == 'Empty' or gene[j] == 'Empty':
                    continue
                else:
                    if len(intersection(gene[i].examinors, gene[j].examinors)) != 0:
                        return False
                    if exists(gene[j].supervisor, gene[i].examinors):
                        return False
                    if exists(gene[i].supervisor, gene[j].examinors):
                        return False
                    if gene[i].supervisor == gene[j].supervisor:
                        return False

    return True


# Function to check soft constraints
def soft_fitness(solution):
    professors = solution.professors
    chromosome = solution.chromosome

    # suppose that score = 0 initially
    score = 0

    # Check if a professor has more than 3 consecutive slots
    # create a list that contains the professors at each time slot from 0 to 11
    professorsofeachslot = []
    for i in range(0, len(chromosome)):
        professorsofeachslot.append([])
        for j in range(0, len(chromosome[i])):
            if chromosome[i][j] != 'Empty':
                professorsofeachslot[i].append(chromosome[i][j].examinors[0])
                professorsofeachslot[i].append(chromosome[i][j].examinors[1])

    # professors having 4 consecutive slots
    professorshavingfourconsecutive = []
    # Check First day
    for i in range(0, 3):
        professorshavingfourconsecutive.extend(
            list(set(professorsofeachslot[i]).intersection(
                set(professorsofeachslot[i + 1]),
                set(professorsofeachslot[i + 2]),
                set(professorsofeachslot[i + 3]),
            ))
        )

    # Check Second day
    for i in range(6, 9):
        professorshavingfourconsecutive.extend(
            list(set(professorsofeachslot[i]).intersection(
                set(professorsofeachslot[i + 1]),
                set(professorsofeachslot[i + 2]),
                set(professorsofeachslot[i + 3]),
            ))
        )

    # professors having 5 consecutive slots

    professorshavingfiveconsecutive = []
    # Check First day
    for i in range(0, 2):
        professorshavingfiveconsecutive.extend(
            list(set(professorsofeachslot[i]).intersection(
                set(professorsofeachslot[i + 1]),
                set(professorsofeachslot[i + 2]),
                set(professorsofeachslot[i + 3]),
                set(professorsofeachslot[i + 4]),
            ))
        )
    # Check Second day
    for i in range(6, 8):
        professorshavingfiveconsecutive.extend(
            list(set(professorsofeachslot[i]).intersection(
                set(professorsofeachslot[i + 1]),
                set(professorsofeachslot[i + 2]),
                set(professorsofeachslot[i + 3]),
                set(professorsofeachslot[i + 4]),
            ))
        )

    # professors having 6 consecutive slots
    professorshavingsixconsecutive = []

    # Check first day
    professorshavingsixconsecutive.extend(
        list(set(professorsofeachslot[0]).intersection(
            set(professorsofeachslot[1]),
            set(professorsofeachslot[2]),
            set(professorsofeachslot[3]),
            set(professorsofeachslot[4]),
            set(professorsofeachslot[5]),
        ))
    )

    # Check second day
    professorshavingsixconsecutive.extend(
        list(set(professorsofeachslot[6]).intersection(
            set(professorsofeachslot[7]),
            set(professorsofeachslot[8]),
            set(professorsofeachslot[9]),
            set(professorsofeachslot[10]),
            set(professorsofeachslot[11]),
        ))
    )

    professorshavingfourconsecutive = diff(professorshavingfourconsecutive, professorshavingfiveconsecutive)
    professorshavingfiveconsecutive = diff(professorshavingfiveconsecutive, professorshavingsixconsecutive)

    score += 1 - (len(professorshavingfourconsecutive) / len(professors))
    score += 0.75 - (len(professorshavingfiveconsecutive) / len(professors))
    score += 0.5 - (len(professorshavingsixconsecutive) / len(professors))

    # TODO: Handle Student Preferences
    for i in range(len(solution.list)):
        if isinstance(solution.list[i], Group):
            if int(solution.list[i].daydesired) == 1:
                grouptimedesired = int(solution.list[i].slotdesired) - 1
                if i < 30:
                    score += 1
            else:
                grouptimedesired = 6 + int(solution.list[i].slotdesired) - 1
                if i >= 30:
                    score += 1
            if grouptimedesired == int(i / 5):
                score += 1

    return score


def diff(li1, li2):
    return list(set(li1) - set(li2))


# Python program to illustrate the intersection
# of two lists in most simple way
def intersection(lst1, lst2):
    lst3 = []
    for prof in lst1:
        for proff in lst2:
            if prof.name == proff.name:
                if prof.name not in lst3:
                    lst3.append(prof.name)
    return lst3


def exists(prof, listt):
    for item in listt:
        if item.name == prof:
            return True
    return False
