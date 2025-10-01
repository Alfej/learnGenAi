from abc import ABC, abstractmethod

class car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def shiftGears(self):
        pass

class Maruti(car):

    def start(self):
        print("Maruti started")

    def stop(self):
        print("Maruti stopped")

    def shiftGears(self):
        print("Maruti shifted gears")
    
if __name__ == "__main__":
    #  from the code we are using the class car without knowing the implementation details of the class Maruti
    m = Maruti()
    m.start()
    m.shiftGears()
    m.stop()
