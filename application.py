from fileSystem.File import File
from fileSystem.Directory import Directory
from Cmd import Cmd

class Application():
    def __init__(self):
        home = Directory("home")
        root = Directory("root", home)
        usr = Directory("usr", home)
        details = Directory("details", usr)
        docs = Directory("docs", details)
        pismo = File("pismo.txt", "Zawartosc pliku pismo.txt")

        home.add_children(root)
        home.add_children(usr)
        usr.add_children(details)
        details.add_children(docs)
        docs.add_children(pismo)

        self.current_directory = home

    def get_current_directory(self):
        return self.current_directory
    
    def get_path(self, current_directory):
        path = current_directory.get_name()
        if current_directory.get_parent() != None:
            path = self.get_path(current_directory.get_parent()) + '/' + path
        return path

    def main(self):
        user_input = ''
        operation = Cmd()
    
        while True:
            path = self.get_path(self.current_directory)
            print(path + ">", end = "")
            user_input = input()
            command_parts = user_input.split(" ")
            user_input = ''
            command = command_parts[0]
            args = command_parts[1:]
            if operation.set_operation(command):
                self.current_directory = operation.execute(self.get_current_directory(), args)
            operation.set_operation('')
            command = ''
            args = []
    
if __name__ == "__main__":
    app = Application()
    app.main()