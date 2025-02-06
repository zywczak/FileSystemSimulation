from fileSystem.Directory import Directory
from commands.operation import operation
import re

class Mkdir(operation):
    def get_operation(self):
        return "mkdir"
    
    def check_and_execute(self, current_directory, *args):
        if len(args) != 1:
            print("Invalid number of arguments")
        else:
            directory = current_directory
            current_directory = self.execute(current_directory, *args)
            if current_directory == None:
                current_directory = directory
        return current_directory
    
    def execute(self, current_directory, *args):
        directory = current_directory
        special_characters = r'[_.$/\\~]'
        directories = args[0].split("/")
        for j in range(len(directories)):
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
                        for i in range(j, len(directories)):
                            if not re.search(special_characters, directories[i]):                    
                                kat = Directory(directories[i], current_directory.get_name())
                                current_directory.add_children(kat)
                                current_directory = kat
                            else:
                                print("cannot create a directory containing special characters")
                        return

        return directory