class Task:

    # Function create Task
    def __init__(self,id,title):
        self.id = id
        self.title = title
        self.status = None

    # Function change status to "Done"
    def changeStatusToDone(self):
        self.status = "Done"

    # Function change status to "To Do"
    def changeStatusToDo(self):
        self.status = "toDo"
