# Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.
# Applicability:
#  - Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem
#  - Use the Facade when you want to structure a subsystem into layers.

from __future__ import annotations

class GraphicalEditor:
    def EditBackGround(self) -> str:
        return "Background edited"

    def EditText(self) -> str:
        return "Text edited"
    
class AudioEditor:
    def EditAudio(self) -> str:
        return "Audio edited"
    

class FacadeVideoEditor:
    def __init__(self):
        self.graphical_editor = GraphicalEditor()
        self.audio_editor = AudioEditor()
    
    def EditVideo(self) -> str:
        return f"{self.graphical_editor.EditBackGround()}, {self.graphical_editor.EditText()}, {self.audio_editor.EditAudio()}"

def client_code() -> None:
    video_editor = FacadeVideoEditor()
    print(video_editor.EditVideo())

if __name__ == "__main__":
    client_code()
    