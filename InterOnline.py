from abc import ABC, abstractmethod

class IOnline(ABC):

    @abstractmethod
    def itemOnline(self)->str:
        pass

    