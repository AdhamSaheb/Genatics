from tkinter import filedialog
import os
from Data import readFiles
from Genetic.generate import generate
from Genetic.Fitness import fitness_function
from Models.Group import Group
import tkinter as tk
from tkinter import ttk

ROOT_DIR = os.path.abspath(os.curdir)
import plotly.graph_objects as go
from Genetic.crossover import *
from Models.Group import Group

import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

# Initializing 2 lists for professors and groups and solutions
professors = []
groups = []
solutions = []
#
numberofiterations = 100


# This is the function we are trying to fit to the data.
def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def openProfDialog(root):
    root.filename = filedialog.askopenfilename(initialdir=ROOT_DIR + "/input", title="Select file",
                                               filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))
    try:
        with open(root.filename, 'r') as UseFile:
            readFiles.readProfessorsFile(UseFile, professors)

    except Exception as e:
        print(e)


def printProfessors():
    names = []
    interests = []
    for professor in professors:
        names.append(professor.name)
        interests.append(professor.subjects)

    fig = go.Figure(data=[go.Table(columnwidth=[300, 300],
                                   header=dict(values=['<b>Professor name<b>', '<b>Area of Interests<b>'],
                                               line_color='darkslategray',
                                               fill_color='lightskyblue',
                                               height=70,
                                               align='center'),
                                   cells=dict(values=[names,  # 1st column
                                                      interests],  # 2nd column
                                              line_color='darkslategray',
                                              fill_color='lightcyan',
                                              height=30,
                                              align='center'))
                          ])

    fig.update_layout(width=1800, height=1800)
    fig.show()


def openGroupsDialog(root):
    root.filename = filedialog.askopenfilename(initialdir=ROOT_DIR + "/input", title="Select file",
                                               filetypes=(("Text Files", "*.txt"), ("all files", "*.*")))
    try:
        with open(root.filename, 'r') as UseFile:
            readFiles.readGroupsFile(UseFile, groups, professors)
    except Exception as e:
        print(e)


def printGroups():
    students = []
    projects = []
    supervisors = []
    daydesired = []
    slotdesired = []
    for group in groups:
        students.append(group.students)
        projects.append(group.project)
        supervisors.append(group.supervisor)
        daydesired.append(group.daydesired)
        slotdesired.append(group.slotdesired)
    fig = go.Figure(data=[go.Table(columnwidth=[450, 450, 450, 50, 50],
                                   header=dict(values=['<b>Students\' names<b>', '<b>Group Project<b>',
                                                       "<b>Group Supervisor<b>", "<b>Day Desiredr<b>",
                                                       "<b>Slot Desired<b>"],
                                               line_color='darkslategray',
                                               fill_color='lightskyblue',
                                               height=70,
                                               align='center'),
                                   cells=dict(values=[students,  # 1st column
                                                      projects, supervisors, daydesired, slotdesired],  # 2nd column
                                              line_color='darkslategray',
                                              fill_color='lightcyan',
                                              height=40,
                                              align='center'))
                          ])

    fig.update_layout(width=1800, height=1800)
    fig.show()





# This is the main loop of the program
x_number_values=[]
y_number_values=[]


# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def goBt(populationEntry):
    global population
    population = int(populationEntry)
    solutions = []
    # Initializing the solutions
    for i in range(population):
        solution = generate(groups, professors)
        solution.fitness = fitness_function(solution)
        solutions.append(solution)
        solutions.sort(key=lambda x: x.fitness, reverse=True)

    for i in range(numberofiterations):
        solutions2 = []
        print("iteration number " , i)

        for j in range(int(population / 2)):  # generating by crossover
            newsolutions = breed_by_crossover3(solutions[0], solutions[j+1], professors)
            solutions2.append(newsolutions[0])
            solutions2.append(newsolutions[1])
        #update fitness and resort
        solutions2.sort(key=lambda x:x.fitness, reverse=True)

        for j in range(int(population / 4)):  # generating by mutation
            tmpsolution = mutate(solutions2[0], professors)
            tmpsolution.fitness = fitness_function(tmpsolution)
            solutions2.append(tmpsolution)

        for j in range(int(population/8)):
            tmpsolution=generate(groups,professors)
            solution.fitness=fitness_function(tmpsolution)
            solutions2.append(tmpsolution)


        solutions = solutions + solutions2
        # update fitness and resort
        for solution in solutions:
            solution.fitness=fitness_function(solution)
        solutions.sort(key=lambda x: x.fitness, reverse=True)
        solutions = solutions[0:population]

        print("Highest fitness so far = ", solutions[0].fitness)

        x_number_values.append(i)
        y_number_values.append(solutions[0].fitness)

    # printing the answer
    final_answer = solutions[0]
    print("Final answer fitness = " , final_answer.fitness)
    final_list = [[], [], [], [], [], [], [], [], [], [], [], [] ]

    i = 0
    for slot in final_answer.chromosome:
        for entry in slot:
            if isinstance(entry, Group):
                st = ''
                st += '<b>' + entry.project + '</b><br> '
                for student in entry.students:
                    st += student + "<br>"
                st += "<b>Supervisor:</b><br>" + entry.supervisor + "<br>"
                st += "<b>Examinors: </b><br>"
                for examinor in entry.examinors:
                    st += examinor.name + "<br>"
                final_list[i].append(st)
            else:
                final_list[i].append(entry)
        i += 1

    fig = go.Figure(data=[go.Table(columnwidth=[500, 500, 500, 500, 500, 500],
                                   header=dict(values=['<b>9:00-10:00<b>', '<b>10:00-11:00<b>', '<b>11:00-12:00<b>',
                                                       "<b>12:00-01:00<b>",
                                                       '<b>01:00-02:00<b>', '<b>02:00-03:00<b>'],
                                               line_color='darkslategray',
                                               fill_color='lightskyblue',
                                               height=70,
                                               align='center'),

                                   cells=dict(values=[final_list[0],  # 1st column
                                                      final_list[1], final_list[2], final_list[3], final_list[4],
                                                      final_list[5]],
                                              line_color='darkslategray',
                                              fill_color='lightcyan',
                                              height=40,
                                              align='center'))
                          ])

    fig.update_layout(width=2500, height=2500, title="Day 1")
    fig.show()

    fig = go.Figure(data=[go.Table(columnwidth=[500, 500, 500, 500, 500, 500],
                                   header=dict(values=['<b>9:00-10:00<b>', '<b>10:00-11:00<b>', '<b>11:00-12:00<b>',
                                                       "<b>12:00-01:00<b>",
                                                       '<b>01:00-02:00<b>', '<b>02:00-03:00<b>'],
                                               line_color='darkslategray',
                                               fill_color='lightskyblue',
                                               height=70,
                                               align='center'),

                                   cells=dict(values=[final_list[6],  # 1st column
                                                      final_list[7], final_list[8], final_list[9], final_list[10],
                                                      final_list[11]],
                                              line_color='darkslategray',
                                              fill_color='lightcyan',
                                              height=40,
                                              align='center'))
                          ])

    fig.update_layout(width=2500, height=2500, title="Day 2")
    fig.show()











    # Draw point based on above x, y axis values.
    plt.plot(x_number_values, y_number_values)

    # Set chart title.
    plt.title("Fitness through time ")
    axes = plt.gca()
    axes.set_xlim([0, 100])
    axes.set_ylim([0, max(y_number_values)+10])

    # Set x, y label text.
    plt.xlabel("Iteration")
    plt.ylabel("Fitness")
    plt.show()
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
def printExaminors(examinors):
    for one in examinors:
        print(one, end=" + ")


def printValidSolutions():
    isThere = False
    for sol in solutions:
        # print("fitness=" ,sol.fitness)
        if sol.fitness > 0:
            print("Solution with fitness ", sol.fitness)

            isThere = True
    if not isThere:
        print("No Valid Solutions!")


# Changes that I have made:
# 1- changed the assign function , there's no way any professsor will get more than 6 now
# 2- removed < 3 term in hard fitness


def popupmsg(msg, title):
    popup = tk.Tk()
    popup.wm_title(title)

    text = ttk.Label(popup, text=msg)
    text.pack(side="top")
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()
