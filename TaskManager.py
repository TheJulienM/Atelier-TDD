import Action
import Task

import sqlite3
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()

class TaskManager:
    def __init__(self, tasks):
        self.tasks = tasks

    def checkUserInput(self,input):
        if input is not None:
            if type(input) is list :
                if input[0] in ["+","-","x","o"] :
                    if input[0] == "+" :
                        return True
                    elif input[0] in ["-","x","o"] :
                        if len(input) > 2 :
                            return False
                        else :
                            try:
                                int(input[1])
                                return True
                            except:
                                return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def parseCommand(self,command):
        command = command.split(" ")
        print(command)
        checkInput = TaskManager.checkUserInput(self,command)
        if checkInput is True :
            commandSize = len(command)
            commandAction = ""
            if(command[0] == "+") :
                for i in range(1,commandSize) :
                    if i != 1 :
                        commandAction = commandAction + " " + command[i]
                    else:
                        commandAction = command[i]
                return Action.Action("add",commandAction)
            elif (command[0] == "-"):
                return Action.Action("del", command[1])
            elif (command[0] == "x"):
                return Action.Action("done", command[1])
            elif (command[0] == "o"):
                return Action.Action("toDo", command[1])
        else:
            return False

    def createTask(self,id,action):
        task = Task.Task(id,action.title)
        (self.tasks).append(task)
        print(self.tasks)
        return task


    def deleteTask(self,id):
        self.tasks.pop(id)
        print(self.tasks)

    def changeTaskStatusToDone(self,id):
        task = self.tasks[id]
        task.changeStatusToDone()
        task.status = "Done"
        print(self.tasks)
        # task.status = "Done"
        # Les deux fonctionnent mais j'avais envie
        # de faire une petite méthode dans ma class Task je la trouvais un peu vide

    def changeTaskStatusToDo(self,id):
        task = self.tasks[id]
        task.changeStatusToDo()
        print(self.tasks)

    def InsertTaskDatabase(self,id,title,status):
        cur.execute("INSERT INTO task(id,title,status) VALUES (?,?,?)", (id,title,status))

        conn.commit()

    def UpdateTaskDatabase(self,id,title,status):
        cur.execute("UPDATE task SET title = ?, status = ? WHERE id = ?", (title,status,id))
        conn.commit()

    def getTaskFromDatabase(self):
        tasksData = cur.execute("SELECT * FROM task")
        tasksData = tasksData.fetchall()
        if len(tasksData) != 0 :
            for taskRow in tasksData:
                task = Task.Task(taskRow[0], taskRow[1])
                task.status = taskRow[2]
                self.tasks.append(task)