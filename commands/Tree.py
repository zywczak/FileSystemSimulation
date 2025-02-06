from commands.operation import operation
from commands.Cd import Cd

class Tree(operation):
    def __init__(self):
        self.depth = 0

    def get_operation(self):
        return "tree"
    
    def check_and_execute(self, current_directory, *args):
        if len(args) > 1:
            print("Invalid number of arguments")
        else:
            current_directory = self.execute(current_directory, *args)
        return current_directory
    
    def execute(self, current_directory, *args):
        if len(args) == 1:
            self.execute_with_parameter(current_directory, *args)
            return current_directory
        self.execute_without_parameter(current_directory)
        return current_directory

    
    def execute_without_parameter(self, current_directory):
        indentation = " " * self.depth * 2
        print(f"{indentation}|_ {current_directory.get_name()}")
        if current_directory.get_type() != "file":
            self.depth += 1
            for child in current_directory.get_children():
                self.execute_without_parameter(child)
            self.depth -= 1
    
    def execute_with_parameter(self, current_directory, *args):
        if len(args) == 1:
            current_directory = Cd().execute(current_directory, args[0])
        if current_directory != None:
            indentation = " " * self.depth * 2
            print(f"{indentation}|_ {current_directory.get_name()}")
            if current_directory.get_type() != "file":
                self.depth += 1
                for child in current_directory.get_children():
                    self.execute_without_parameter(child)
                self.depth -= 1