from abc import ABC, abstractmethod

class IMultimedia(ABC):

    @abstractmethod
    def ItemMultimedia(self)->str:
        pass
    

class IOnline(ABC):

    @abstractmethod
    def itemOnline(self)->str:
        pass

    