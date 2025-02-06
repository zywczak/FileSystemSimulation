class File():
    def __init__(self, name, content):
        self.type = "file"
        self.content = content
        self.name = name

    def get_content(self):
        return self.content
    
    def set_content(self, content):
        self.content = content
    
    def get_type(self):
        return self.type

    def get_name(self):
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent


    
    
    
        