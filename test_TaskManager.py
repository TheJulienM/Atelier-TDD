import TaskManager
import Task
import Action

def test_createTaskWithTaskManagerWithNoTask() :
    taskManager = TaskManager.TaskManager([])
    assert taskManager.tasks == []

def test_checkValidUserInput() :
    taskManager = TaskManager.TaskManager([])

    inputPlusGood = "+ Add fantastic task"
    boolTrue = taskManager.checkUserInput(inputPlusGood.split(" "))
    assert boolTrue == True

    inputMinusGood = "- 1"
    boolTrue = taskManager.checkUserInput(inputMinusGood.split(" "))
    assert boolTrue == True

    inputCrossGood = "x 1"
    boolTrue = taskManager.checkUserInput(inputCrossGood.split(" "))
    assert boolTrue == True

    inputRoundGood = "o 1"
    boolTrue = taskManager.checkUserInput(inputRoundGood.split(" "))
    assert boolTrue == True

def test_test_checkInvalidUserInput():
    taskManager = TaskManager.TaskManager([])

    inputMinusBad = "- Remove"
    boolFalse = taskManager.checkUserInput(inputMinusBad.split(" "))
    assert boolFalse == False

    inputCrossBad= "x My task is done !"
    boolFalse = taskManager.checkUserInput(inputCrossBad.split(" "))
    assert boolFalse == False

    inputRoundGood = "o I've to do this one !"
    boolFalse = taskManager.checkUserInput(inputRoundGood.split(" "))
    assert boolFalse == False

    inputWithoutType = "Learn PyTest tomorrow"
    boolFalse = taskManager.checkUserInput(inputWithoutType.split(" "))
    assert boolFalse == False

    emptyInput = ""
    boolFalse = taskManager.checkUserInput(emptyInput.split(" "))
    assert boolFalse == False

def test_parseValidCommand() :
    taskManager = TaskManager.TaskManager([])

    inputPlus = "+ Learn C++"
    action = taskManager.parseCommand(inputPlus)
    assert action.type == "add"
    assert action.title == "Learn C++"

    inputMinus = "- 1"
    action = taskManager.parseCommand(inputMinus)
    assert action.type == "del"
    assert action.title == "1"

    inputCross = "x 1"
    action = taskManager.parseCommand(inputCross)
    assert action.type == "done"
    assert action.title == "1"

    inputRound = "o 1"
    action = taskManager.parseCommand(inputRound)
    assert action.type == "toDo"
    assert action.title == "1"

def test_parseInValidCommand() :
    taskManager = TaskManager.TaskManager([])

    inputMinus = "- Learn C++"
    action = taskManager.parseCommand(inputMinus)
    assert action is False

    inputMinus = "x Learn C++"
    action = taskManager.parseCommand(inputMinus)
    assert action is False

    inputMinus = "o Learn C++"
    action = taskManager.parseCommand(inputMinus)
    assert action is False

def test_createAddTask() :
    taskManager = TaskManager.TaskManager([])
    nbTask = len(taskManager.tasks)
    input = "+ Finish my book"
    action = taskManager.parseCommand(input)
    assert action.type == "add"
    if (action.type == "add") :
        task = taskManager.createTask(nbTask,action)
        assert task.id == 0
        assert task.title == "Finish my book"
        assert taskManager.tasks[task.id] == task
        assert len(taskManager.tasks) == 1

def test_deleteTask() :
    taskManager = TaskManager.TaskManager([])
    nbTask = len(taskManager.tasks)
    input = "+ Make a backup of my VPS"
    action = taskManager.parseCommand(input)
    assert action.type == "add"
    if (action.type == "add") :
        task = taskManager.createTask(nbTask,action)
        assert task.id == 0
        assert task.title == "Make a backup of my VPS"
        assert taskManager.tasks[task.id] == task
        print(taskManager.tasks[task.id])
        taskManager.deleteTask(0)
        assert len(taskManager.tasks) == 0

def test_UpdateTaskToDone() :
    taskManager = TaskManager.TaskManager([])
    nbTask = len(taskManager.tasks)
    input = "+ Watch the Synder's Cut"
    action = taskManager.parseCommand(input)
    assert action.type == "add"
    if (action.type == "add") :
        task = taskManager.createTask(nbTask,action)
        assert task.id == 0
        assert task.title == "Watch the Synder's Cut"
        assert taskManager.tasks[task.id] == task
        assert task.status is None
        taskManager.changeTaskStatusToDone(task.id)
        assert task.status == "Done"

def test_UpdateTaskToDo() :
    taskManager = TaskManager.TaskManager([])
    nbTask = len(taskManager.tasks)
    input = "+ I really have to do this one"
    action = taskManager.parseCommand(input)
    assert action.type == "add"
    if (action.type == "add") :
        task = taskManager.createTask(nbTask,action)
        assert task.id == 0
        assert task.title == "I really have to do this one"
        assert taskManager.tasks[task.id] == task
        assert task.status is None
        taskManager.changeTaskStatusToDo(task.id)
        assert task.status == "toDo"




