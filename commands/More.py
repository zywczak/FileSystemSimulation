from commands.operation import operation

class More(operation):
    def get_operation(self):
        return "ls"
    
    def check_and_execute(self, current_directory, *args):
        if len(args) != 1:
           print("Invalid number of arguments!")
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
                    
        j = len(directories)  
        children = current_directory.get_children()
        for child in children:
            if directories[-1] == child.get_name() and child.get_type() == "file":
                print(child.get_content())
                break
            elif directories[-1] == child.get_name() and child.get_type() != "file":
                print(f'{directories[j - 1]} is not file')
                return
            else:
                print(f'{directories[j - 1]} file not found')
                return
        
        return directory