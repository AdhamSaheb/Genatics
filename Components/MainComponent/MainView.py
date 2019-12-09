# Classes
from Components.MainComponent.MainController import *
from Models.Group import Group
from Models.Professor import Professor

# Reading Data From Files
from Data import readFiles

# GUI stuff
from tkinter import *
import tkinter as tk
from tkinter.ttk import *



# Initiallize GUI
root = Tk()

# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
root.geometry("700x250+{}+{}".format(positionRight, positionDown))

root.title("Genetic Algorithm")


# Gets the requested values of the height and widht.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()

# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight-300, positionDown))




style = Style()
style.configure('TButton', font = ('calibri', 20, 'bold'), borderwidth = '4')



# -------------------------------------------------------------------------------------
# everything before this line is relates to the GUI appearance
professorsFileBT = Button(root, text="Select Professors File", command=lambda: openProfDialog(root),width=20)
professorsFileBT.place(x=20,y=10)



professorsPrintBT = Button(root, text="See Professors List", command=printProfessors,width=20)

professorsPrintBT.place(x=370,y=10)
columnwidth = [400,400]
groupsFileBT = Button(root, text="Select Groups File", command=lambda: openGroupsDialog(root),width=20)
groupsFileBT.place(x=20,y=50)

groupsPrintBT = Button(root, text="See Groups List", command=printGroups,width=20)
groupsPrintBT.place(x=370,y=50)

populationLabel = Label(root, text="Enter number of populations desired",font = "Helvetica 16 bold ")
populationLabel.place(x=220,y=120)

populationEntry = Entry(root,width=20)
populationEntry.place(x=250,y=150)

goBT = Button(root, text="Start", command=lambda: goBt(populationEntry.get()),width=20)
goBT.place(x=200,y=200)


# Run Program Forever
root.mainloop()
