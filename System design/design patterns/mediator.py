# Mediator is a behavioral design pattern that lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object
# The Mediator pattern suggests that you should cease all direct communication between the components which you want to make independent of each other. Instead, these components must collaborate indirectly, by calling a special mediator object that redirects the calls to appropriate components
#  the components depend only on a single mediator class instead of being coupled to dozens of their colleagues

# Applicability
# Use the Mediator pattern when it’s hard to change some of the classes because they are tightly coupled to a bunch of other classes.
# Use the pattern when you can’t reuse a component in a different program because it’s too dependent on other components.
# Use the Mediator when you find yourself creating tons of component subclasses just to reuse some basic behavior in various contexts.

from __future__ import annotations
from abc import ABC
import re

class Mediator(ABC):
    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, email: Email, password: Password, submit: Submit, cancel: Cancel) -> None:
        self._email = email
        self._password = password
        self._submit = submit
        self._cancel = cancel
        self._email.set_mediator(self)
        self._password.set_mediator(self)
        self._submit.set_mediator(self)
        self._cancel.set_mediator(self)

    def notify(self, sender: object, event: str) -> None:
        if sender.name == "Submit":
            if event == "FormSubmitted":
                if self._email.validate() and self._password.validate():
                    print(f"Form submitted with Email: {self._email._email} and Password: {self._password._password}")
        elif sender.name == "Cancel":
            if event == "FormCancelled":
                self._email.clear()
                self._password.clear()
                print("Form cleared")

class Component(ABC):
    def set_mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Email(Component):
    def __init__(self) -> None:
        self.name = "Email"

    def validate(self) -> bool:
        EMAIL_REGEX = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(EMAIL_REGEX, self._email) is not None

    def clear(self) -> None:
        self._email = ""

class Password(Component):
    def __init__(self) -> None:
        self.name = "Password"
    def validate(self) -> bool:
        if len(self._password) > 8 and any(char.isdigit() for char in self._password) and any(char.isupper() for char in self._password) and any(char.islower() for char in self._password):
            return True
        return False

    def clear(self) -> None:
        self._password = ""

class Submit(Component):
    def __init__(self) -> None:
        self.name = "Submit"

    def submit_form(self) -> None:
        if self._mediator:
            self._mediator.notify(self, "FormSubmitted")

class Cancel(Component):
    def __init__(self) -> None:
        self.name = "Cancel"

    def cancel_form(self) -> None:
        if self._mediator:
            self._mediator.notify(self, "FormCancelled")


if __name__ == "__main__":
    email = Email()
    password = Password()
    submit = Submit()
    cancel = Cancel()

    mediator = ConcreteMediator(email, password, submit, cancel)

    # Simulate user input
    email._email = "test@example.com"
    password._password = "Password123"

    submit.set_form_data(email._email, password._password)
    submit.submit_form()

    cancel.cancel_form()