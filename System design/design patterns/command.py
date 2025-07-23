# Command is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.

# Applicability:
# Use the Command pattern when you want to parametrize objects with operations.
# Use the Command pattern when you want to queue operations, schedule their execution, or execute them remotely.
# Use the Command pattern when you want to implement reversible operations
from __future__ import annotations
from abc import ABC, abstractmethod

class command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
class print_command(command):
    def __init__(self, message):
        self._message = message

    def execute(self):
        print(f"Executing Print: {self._message}")

class save_File_command(command):
    def __init__(self, receiver, filename, save_path):
        self._receiver = receiver
        self._filename = filename
        self._save_path = save_path

    def execute(self):
        print(f"Executing Save File: {self._filename} to {self._save_path}, Handling  over to receiver for actual saving.")
        self._receiver.save_file(self._filename, self._save_path)

class file_receiver:
    def save_file(self, filename, save_path):
        print(f"File '{filename}' saved at '{save_path}'.")

class command_invoker:
    def __init__(self):
        self._commands = []

    def add_command(self, command: command):
        self._commands.append(command)

    def execute_commands(self):
        for cmd in self._commands:
            cmd.execute()
        self._commands.clear()

if __name__ == "__main__":
    invoker = command_invoker()

    # Adding print command
    print_cmd = print_command("Hello, World!")
    invoker.add_command(print_cmd)

    # Adding save file command
    receiver = file_receiver()
    save_cmd = save_File_command(receiver, "example.txt", "/path/to/save")
    invoker.add_command(save_cmd)

    # Executing all commands
    invoker.execute_commands()

