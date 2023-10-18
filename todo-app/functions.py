import os
import sys
FILEPATH = "files/todos.txt";

def get_todos(path = FILEPATH):
    """returns list of to-dos in a text file"""
    with open(path, 'r') as file:
        todos = file.readlines()
        return todos

def write_todos( todos: list, path = FILEPATH):
    """write to-dos to a textfile"""
    with open(path, 'w') as file:
        file.writelines(todos)

def Add( todo_list: list, path = FILEPATH):
    """Append item to to-dos"""
    if not os.path.exists(path):
        with open(path, 'w') as file:
            file.writelines(todo_list)
            
    else:
        file_todos = get_todos()    
                    
        # append to file_items
        for todo in todo_list:
            file_todos.append(todo)
                    
        write_todos(file_todos)

def Show(path = FILEPATH):
    """prints to-dos"""
    if not os.path.exists(FILEPATH):
        print("You have no todo items.");
        sys.exit();

    file_todos = get_todos()
            
    [print(str(index) + ">",todo.capitalize().strip('\n',)) for index, todo in enumerate(file_todos, start=1)];

def Edit(todo_item: str, todo_index_input: int, path = FILEPATH):
    """Edits item on to-do list"""
    if not os.path.exists(path):
        print("You have no todo items to edit.");
        sys.exit();

    file_todos = get_todos()  
                
    # edit to file_items
    file_todos[todo_index_input - 1] = todo_item;
    
    write_todos(file_todos)

def Remove(todo_index_input: str, path = FILEPATH):
    """Removes item on to-do list"""
    file_todos = get_todos()   
                
    # rmeove file_items
    removed_todo = file_todos.pop(int(todo_index_input) - 1).strip('\n');

    # delete file if empty
    if len(file_todos) == 0:
        os.remove(path);
    else:
        write_todos(file_todos)

    # narration
    print(f"The todo '{removed_todo}' has been removed from your todo list.");

def Exit(name_input: str):
    """Exits to-do program"""
    print("Goodbye, " + name_input.capitalize() + "!");
    sys.exit();
