from commands.operation import operation
from commands.Cd import Cd
from commands.Cp import Cp
from commands.Ls import Ls
from commands.Mkdir import Mkdir
from commands.Mv import Mv
from commands.Tree import Tree
from commands.More import More

class Cmd():
    def __init__(self):
        pass

    def set_operation(self, operation):
        class_name = operation.capitalize()
        if class_name == '':
            return False
        elif class_name in globals():
            self.operation = globals()[class_name]()
            return True
        else:
            print(f"Unknown {class_name} operation!")
            return False

    def get_operation(self):
        return self.operation
    
    def execute(self, current_directory, args):
        directory = self.get_operation().check_and_execute(current_directory, *args)
        current_directory = directory
        return current_directory