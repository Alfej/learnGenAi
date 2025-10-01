class Maruti():
    def __init__(self):
        self.__mySpeed = 0

    def start(self):
        self.__mySpeed = 5
        print("Maruti started moving at speed", self.__mySpeed)

    def stop(self):
        self.__mySpeed = 0
        print("Maruti stopped moving at speed", self.__mySpeed)

    def shiftGears(self):
        self.__mySpeed += 10
        print("Maruti shifted gears to speed", self.__mySpeed)
    
    def getSpeed(self):
        return self.__mySpeed

if __name__ == "__main__":
    #  from the code we are using the class car without knowing the implementation details of the class Maruti
    m = Maruti()
    m.start()
    m.shiftGears()
    print("Current speed is", m.getSpeed())
    m.stop()
    # It is important to remember that Python relies heavily on developer convention and trust for managing variable access, rather than strict enforcement mechanisms.
    # m.__mySpeed = 1000  # direct access to the attribute
    # print("Maruti speed changed to", m.__mySpeed)