from abc import ABC, abstractmethod

class Describable(ABC):
    def __init__(self):

    @abstractmethod
    def describe(self):
        return str