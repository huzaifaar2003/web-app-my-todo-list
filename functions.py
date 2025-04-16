def read_todos(filepath = "todo_list.txt"): #default parameter for filepath
    """Doc String for read_todos.
        Read a file and return a to-do list.
    """
    with open(filepath, "r") as todo_list_file_local:
        todo_list_local = todo_list_file_local.readlines()
    return todo_list_local

print(help(read_todos),"\n")

def write_todos(todo_list, filepath = "todo_list.txt"):
    """Doc String for write_todos.
            Write the latest to-do list to a text file.
        """
    with open(filepath, "w") as todo_list_file_local:
        todo_list_file_local.writelines(todo_list)
    return todo_list_file_local

print(help(write_todos),"\n")
