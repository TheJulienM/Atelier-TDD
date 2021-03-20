import TaskManager
import Task
import Action
import sqlite3
import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

with sqlite3.connect(db_path) as conn:
    cur = conn.cursor()

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

def test_printTaskList() :
    # Pour simplifier le test nous allons créés plusieurs tâches
    # qui seront toujours correctement déclarées par l'utilisateur
    taskManager = TaskManager.TaskManager([])
    nbTask = len(taskManager.tasks)
    input_1 = "+ Task one"
    action_1 = taskManager.parseCommand(input_1)
    task_1 = taskManager.createTask(nbTask, action_1)
    assert len(taskManager.tasks) == 1 and taskManager.tasks[0] == task_1
    input_2 = "+ Task two"
    action_2 = taskManager.parseCommand(input_2)
    nbTask = len(taskManager.tasks)
    task_2 = taskManager.createTask(nbTask, action_2)
    assert len(taskManager.tasks) == 2 and taskManager.tasks[1] == task_2
    taskManager.changeTaskStatusToDone(task_1.id)
    assert task_1.status == "Done"
    taskManager.changeTaskStatusToDone(task_2.id)
    assert task_2.status == "Done"

# Information :
# Par soucis de temps les Task créées dans les tests précédents ne sont pas
# enregitrées dans la base, seulement les prochaines le seront.
def test_TaskAndDatabase() :
    # On vide la table task de la base de données
    cur.execute("DELETE FROM task")
    conn.commit()
    taskManager = TaskManager.TaskManager([])
    nbTask = len(taskManager.tasks)
    input = "+ Upload this task to database"
    action = taskManager.parseCommand(input)
    task = taskManager.createTask(nbTask, action)
    assert task.id == 0
    assert task.title == "Upload this task to database"
    assert taskManager.tasks[task.id] == task
    taskManager.InsertTaskDatabase(task.id,task.title,task.status)
    assert len(taskManager.tasks) == 1
    idData = cur.execute("SELECT id FROM task WHERE id = 0")
    assert (idData.fetchone())[:][0] == task.id
    titleData = cur.execute("SELECT title FROM task where id = ?", (task.id,))
    assert (titleData.fetchone())[:][0] == task.title
    statusData = cur.execute("SELECT status FROM task where id = ?", (task.id,))
    assert (statusData.fetchone())[:][0] == task.status
    taskManager.changeTaskStatusToDo(task.id)
    assert task.status == "toDo"
    taskManager.UpdateTaskDatabase(task.id,task.title,task.status)
    idData = cur.execute("SELECT id FROM task where id = ?", (task.id,))
    assert (idData.fetchone())[:][0] == task.id
    titleData = cur.execute("SELECT title FROM task where id = ?", (task.id,))
    assert (titleData.fetchone())[:][0] == task.title
    statusData = cur.execute("SELECT status FROM task where id = ?", (task.id,))
    assert (statusData.fetchone())[:][0] == task.status
    conn.commit()

    assert len(taskManager.tasks) == 1

    # On imagine une déconnexion de l'utilisateur, la liste local est donc vidée pour simuler un relancement du programme
    taskManager.tasks = []
    assert len(taskManager.tasks) == 0
    taskManager.getTaskFromDatabase()
    assert len(taskManager.tasks) != 0
    task = taskManager.tasks[0]
    assert task.id == 0
    assert task.title == "Upload this task to database"
    assert task.status == "toDo"

    # On vide la table task de la base de données
    # Bien sûr on imagine qu'on aurait une base pour les tests afin de ne pas
    # supprimer les données en production
    cur.execute("DELETE FROM task")
    conn.commit()




