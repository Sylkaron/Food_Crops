from abc import ABC, abstractmethod

class Describable(ABC):
    def __init__(self):
        super(Describable, self).__init__()

    @abstractmethod
    def describe(self):
        pass