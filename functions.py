FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items"""
    try:
        with open(filepath, 'r') as file:
            todos = file.readlines()
            # Remove newline characters from each todo item
            todos = [todo.strip() for todo in todos]
            return todos
    except FileNotFoundError:
        # Return empty list if file doesn't exist
        return []


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list to the text file"""
    with open(filepath, 'w') as file:
        # Add newlines when writing
        for todo in todos_arg:
            file.write(todo + '\n')


if __name__ == "__main__":
    print('hello')
    
    # Example usage:
    todos = get_todos()
    print("Current todos:", todos)
    
    # Add a new todo
    todos.append("Buy groceries")
    write_todos(todos)
    
    # Read and display updated todos
    updated_todos = get_todos()
    print("Updated todos:", updated_todos)