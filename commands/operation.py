from abc import ABC, abstractmethod

class operation(ABC):
    @abstractmethod
    def get_operation(self):
        pass

    @abstractmethod
    def check_and_execute(self, current_directory):
        pass

    @abstractmethod
    def execute(self, current_directory):
        pass