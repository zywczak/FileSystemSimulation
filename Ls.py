from operation import operation
from Cd import Cd

class Ls(operation):
    def get_operation(self):
        return "ls"
    
    def check_and_execute(self, current_directory, *args):
        if len(args) > 1:
           print("Invalid number of arguments!")
        else:
            current_directory = self.execute(current_directory, *args)
        return current_directory
    
    def execute(self, current_directory, *args):
        directory = current_directory
        if len(args) == 1:
            current_directory = Cd().execute(current_directory, *args)
            if current_directory != None:
                current_directory.display()
        else:
            current_directory.display()
        return directory