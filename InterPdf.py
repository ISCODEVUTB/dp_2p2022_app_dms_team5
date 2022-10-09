from abc import ABC, abstractmethod

class IPdf(ABC):

    @abstractmethod
    def operaciones(self)->str:
        pass
    