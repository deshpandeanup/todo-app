FILEPATH = r"C:\Users\anupd\Python Scripts\todos.txt"


def get_todos(filepath=FILEPATH):
    """" Reads a text file provided as a parameter/argument
    defined in the global variable FILEPATH
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """" Writes the to-do items list in the text file defined in the global variable
    FILEPATH
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

