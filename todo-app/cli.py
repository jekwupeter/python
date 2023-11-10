import sys;
import datetime
from functions import Add, Show, Edit, Remove, Exit;
from auth import Login

name_prompt = "Enter your user name:";
name_input = input(name_prompt);
password_prompt = "Enter your password:";
password_input = input(password_prompt);

auth_limit = 0;
validated = False;
while(auth_limit < 3):
    auth_limit += 1;
    if not Login(name_input, password_input):       
        print("invalid credentials. Please try again.\n");
        name_input = input(name_prompt);
        password_input = input(password_prompt);
    else:
        validated = True;
        break;

if not validated:
    print("You have exceeded the number of attempts. Please try again later.");
    sys.exit();

print("Hello, " + name_input.capitalize()  + "!");
print("The time is", datetime.datetime.now());
# .strftime("%H:%M:%S")

# todo logic(add, show, exit)

while True:
    user_action = input("Type add, show, edit, remove or exit:");
    user_action = user_action.strip().lower();

    # check if user is using quick add or edit
    split_user_action = user_action.split(" ");
    if len(split_user_action) > 1:
        if user_action.startswith("add"):
            new_item = user_action[4:]
            Add([new_item + "\n"]);
            continue;

        elif user_action.startswith("edit"):
            try:
                todo_index_input = int(split_user_action[1]);
                new_todo_prompt = "Please enter the new todo item:";
                new_todo = input(new_todo_prompt) + "\n";
                Edit(new_todo, todo_index_input)
                continue;
            except ValueError:
                print("Invalid input. Please try again with index number.");
                continue;
            except IndexError:
                print("Invalid index. Please try again.");
                continue;

        elif user_action.startswith("remove"):
            try:
                todo_index_input = int(split_user_action[1]);
                Remove(todo_index_input)
                continue;
            except IndexError:
                print("Invalid index. Please try again.");
                continue;

    match user_action:
        case "add":
            todo_count_prompt = "Please enter number(0-3) of todo items you want to input:";
            todo_count_input = input(todo_count_prompt);

            if int(todo_count_input) < 0 or int(todo_count_input) > 3:
                count_exceeded_error = "You have exceeded the number of todo items you can input. Please try again.";
                print(count_exceeded_error);
                sys.exit();

            todo_list = [];
            for i in range(0, int(todo_count_input)):
                # get user input
                todo_prompt = "Please enter todo item #" + str(i+1) + ":";
                todo_input = input(todo_prompt);
                todo_list.append(todo_input + "\n");
            
            Add(todo_list)
                
        case "show":
            print("Here is your todo list:");
            
            Show()

        case "edit":
            todo_edit_prompt = "Please enter the index of the todo item you want to edit:";
            todo_index_input = input(todo_edit_prompt);
            new_todo_prompt = "Please enter the new todo item:";
            new_todo = input(new_todo_prompt) + "\n";
        
            Edit(new_todo, todo_index_input)
            
        case "remove":
            todo_remove_prompt = "Please enter the index of the todo item you want to remove:";
            todo_index_input = input(todo_remove_prompt);
            Remove(todo_index_input)

        case "exit":
            Exit(name_input)

        case _:
            print("Invalid input. Please try again.");
