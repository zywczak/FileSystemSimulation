class Directory():
    def __init__(self, name, parent = None):
        self.name = name
        self.type = "directory"
        self.parent = parent
        self.children = []

    def add_children(self, child):
        self.children.append(child)

    def display(self):
        for child in self.children:
            print(child.get_name())

    def remove_children(self, child):
        self.children.remove(child)

    def get_type(self):
        return self.type

    def get_children(self):
        children = []
        for i in range(len(self.children)):
            children.append(self.children[i])
        return children
    
    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
    
