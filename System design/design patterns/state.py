# State is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.
# Applicability:
# Use the State pattern when you have an object that behaves differently depending on its current state, the number of states is enormous, and the state-specific code changes frequently
# Use the pattern when you have a class polluted with massive conditionals that alter how the class behaves according to the current values of the class’s fields.
#  Use State when you have a lot of duplicate code across similar states and transitions of a condition-based state machine
from __future__ import annotations
from abc import ABC, abstractmethod

class PhoneContext:
    _state = None

    def __init__(self,state):
        self.transition_to(state)

    def transition_to(self,state):
        print(f"Context: phone {type(state).__name__}")
        self._state = state
        self._state.context = self


    def lock_phone(self):
        self._state.handle_lock()

    def unlock_phone(self):
        self._state.handle_unlock()


class state(ABC):
    @property
    def context(self):
        return self._context
    
    @context.setter
    def context(self, contex):
        self._context = contex

    @abstractmethod
    def handle_lock(self):
        pass

    @abstractmethod
    def handle_unlock(self):
        pass
        
class Lock(state):
    def handle_lock(self):
        print("Phone already in lock State")

    def handle_unlock(self):
        print("Unlocking the phone!!")
        print("changing state from lock to unlock")
        self._context.transition_to(Unlock())
    
class Unlock(state):
    def handle_unlock(self):
        print("Phone already in Unlock State")

    def handle_lock(self):
        print("locking the phone!!")
        print("changing state from unlock to lock")
        self._context.transition_to(Lock())
    
if __name__=="__main__":
    PhoneCon = PhoneContext(Lock())
    PhoneCon.unlock_phone()
    PhoneCon.lock_phone()