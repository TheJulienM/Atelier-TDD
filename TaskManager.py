import Action

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

