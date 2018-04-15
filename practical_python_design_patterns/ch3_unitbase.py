from abc import ABCMeta, abstractmethod

class UnitBase(metaclass=ABCMeta):

    @abstractmethod
    def clone(self):
        pass
