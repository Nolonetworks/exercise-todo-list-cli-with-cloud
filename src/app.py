import json, requests
todos = []
urlAPI = "https://assets.breatheco.de/apis/fake/todos"

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    global todos
    data = {
        "label" : title,
        "done" : False
    }
    todos.append(data)
    return "agregaste la tarea"

def print_list():
    # your code here
    global todos
    for item in todos:
        print(item)

def delete_task(number_to_delete):
    # your code here
    number_to_delete = int(number_to_delete) - 1
    todos.pop(number_to_delete)
    return todos

def initialize_todos():
    global todos
    headers = {
    'Content-Type':'application/json'
    }
    r = requests.get('https://assets.breatheco.de/apis/fake/todos/user/manuel04') 
    if(r.status_code == 404):
        print("No previous todos found, starting a new todolist")
        r = requests.post(url = 'https://assets.breatheco.de/apis/fake/todos/user/manuel04', headers=headers, data = json.dumps([]))
        if r.status_code == 200:
            print("Tasks initialized successfully")
    else:
        print("A todo list was found, loading the todos...")
        todos = r.json()

    
def save_todos():
    # your code here
    global todos
    headers = {
    'Content-Type':'application/json'
    }
    req = requests.put(urlAPI + "/user/manuel04", headers=headers, data=json.dumps(todos))

    print(req.json())

def load_todos():
    # your code here
    global todos
    headers = {
    'Content-Type':'application/json'
    }
    req = requests.get(urlAPI + "/user/manuel04", headers=headers)

    if req.status_code == 200:
        todos = req.json()
    else:
        print(req.json())
    
# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    stop = False
    print("Initializing todos with previous data or creating a new todo's list...")
    initialize_todos()
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Send/Save todo's to API
        5. Retrieve todo's from API
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")