import Task

def test_createTask():
    id = 0
    title = "Title 0"
    status = None
    task_0 = Task.Task(id,title,status)
    assert task_0.id == 0
    assert task_0.title == "Title 0"
    assert task_0.status == None

def test_changeStatusToDo():
    id = 1
    title = "Title 1"
    status = None
    task_1 = Task.Task(id,title,status)
    task_1.changeStatusToDo()
    assert task_1.status == "toDo"

def test_changeStatusDone():
    id = 2
    title = "Title 2"
    status = None
    task_2 = Task.Task(id,title,status)
    task_2.changeStatusToDone()
    assert task_2.status == "Done"

