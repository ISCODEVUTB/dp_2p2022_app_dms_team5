from abc import ABC, abstractmethod

class IMultimedia(ABC):

    @abstractmethod
    def ItemMultimedia(self)->str:
        pass
    