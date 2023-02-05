# function to get to-do
def get_todos():
    file = open('todos.txt')
    todos = file.readlines()
    file.close()
    return todos

# function to print list
def print_todos(todos):
    for index, item in enumerate(todos):
        item = item.strip('\n')
        print(f"{index + 1}. {item}")


# function to save todos
def save_todos(todos):
    file = open('todos.txt', 'w')
    file.writelines(todos )
    file.close()