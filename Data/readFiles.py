from Models.Professor import Professor
from Models.Professor import validdoctors
from Models.Group import Group


def readProfessorsFile(professorsFile, professors):
    for x in professorsFile:
        if x == '\n':
            continue
        else:
            s = x.split(":")  # splitting the line for name and subjects
            name = s[1][:-1]
            subjects = s[0].split(",")
            professor = Professor(name, subjects)
            professors.append(professor)


def readGroupsFile(groupsFile, groups, professors):
    # Reading the groups file and creating objects of them
    for x in groupsFile:
        valideximinors = []
        examinors = []

        if x == '\n':
            continue
        else:
            s = x.split(":")
            students = s[0].split(",")
            project = s[1]
            subjects = s[2].split(",")
            supervisor = s[3]
            daydesired = s[4]
            timedesired = s[5]

            group = Group(students, project, supervisor, subjects, examinors, valideximinors,daydesired,timedesired)
            group.validexaminors = validdoctors(group, professors)  # provide a list of valid doctors for each group
            groups.append(group)
