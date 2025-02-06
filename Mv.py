from operation import operation
from Cd import Cd
import copy

class Mv(operation):
    def get_operation(self):
        return "cp"

    def check_and_execute(self, current_directory, *args):
        if len(args) != 2:
            print("Invalid number of arguments")
        else:
            directory = current_directory
            current_directory = self.execute(current_directory, *args)
            if current_directory == None:
                current_directory = directory
        return current_directory

    def execute(self, current_directory, *args):
        directory = current_directory
        directories = args[0].split("/")
        for j in range(len(directories) - 1):
            if j == 0 and directories[0] == ".":
                continue
            if j == 0 and directories[0] == "~":
                while True:
                    if current_directory.get_parent() != None:
                        current_directory = current_directory.get_parent()
                    else:
                        break
                continue
            if directories[j] == "..":
                if current_directory.get_parent() != None:
                    current_directory = current_directory.get_parent()
                else:
                    print('folder not found')
                    return   
            else:
                children = current_directory.get_children()
                for child in children:
                    if directories[j] == child.get_name() and child.get_type() != "file":
                        current_directory = child
                        break
                    elif directories[j] == child.get_name() and child.get_type() == "file":
                        print(f'{directories[j]} is file')
                        return
                    else:
                        print(f'{directories[j]} directory not found')
                        return
                      
        children = current_directory.get_children() 
        for child in children:
            if directories[-1] == child.get_name():
                to_move = copy.deepcopy(child)
                break
            else:
                print(f'{directories[-1]} not found')
                return
        
        from_directory = current_directory
        current_directory = directory
        current_directory = Cd().execute(current_directory, args[1])

        if current_directory != None:
            i = False
            for child in current_directory.get_children():
                if child.get_name() == to_move.get_name():
                    i = True
                    print('this is in directory')
                    break
            if i == False:
                to_move.set_parent(current_directory)
                current_directory.add_children(to_move)
                from_directory.remove_children(to_move)
        else:
            print('directory not found')       
        
        current_directory = directory
        return current_directory