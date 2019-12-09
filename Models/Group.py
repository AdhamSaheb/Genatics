class Group:
    def __init__(self, students,project,supervisor,subjects,examinors,validexaminors,daydesired,slotdesired):
        self.students=students
        self.supervisor=supervisor
        self.project=project
        self.subjects=subjects
        self.examinors=examinors
        self.validexaminors=validexaminors # these are the doctors that have at least one interest in the project and are not the supervisor
        self.daydesired = daydesired
        self.slotdesired = slotdesired

    def __str__(self):
        names=''
        for i in range(len(self.examinors)):
            if i == len(self.examinors)-1:
                names=names+self.examinors[i].name
            else:
                names = names + self.examinors[i].name+"|"

        if self.examinors:
            return str(self.students) +" "+str(self.supervisor)+" "+str(self.project)+" "+str(self.subjects)+" Examinors: ["+names+"], Day: " + str(self.daydesired) + " slot: " + self.slotdesired
        else:
            return str(self.students) + " " + str(self.supervisor) + " " + str(self.project) + " " + str(self.subjects) + "Day: " + str(self.daydesired) + " slot: " + self.slotdesired
