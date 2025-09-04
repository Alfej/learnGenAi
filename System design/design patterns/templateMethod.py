# Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

#Applicability
#  Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.
# Use the pattern when you have several classes that contain almost identical algorithms with some minor differences. As a result, you might need to modify all classes when the algorithm changes.


class DisplayContentTemplate():

    def DisplayContent(self,path):
        self.mine(path)
        self.openFile()
        self.extactData()
        self.parseData()
        self.Display()
        self.close()

    def mine(self,path):
        print(f"Mining the file located at {path}")
    
    def openFile(self):
        print("Opening File")
    def extactData(self):
        print("Extracting Data")
    def parseData(self):
        print("Parsing Data")
    def Display(self):
        print("Display Parsed Data")
    def close(self):
        print("Closing File")

class DisplayMDContent(DisplayContentTemplate):

    def openFile(self):
        print("Opening MarkdownFile File")
    def extactData(self):
        print("Extracting Data from MarkdownFile")
    def parseData(self):
        print("Parsing Data from MarkdownFile")
    def close(self):
        print("Closing MarkdownFile File\n\n") 

class DisplayHTMLContent(DisplayContentTemplate):

    def openFile(self):
        print("Opening HTML File")
    def extactData(self):
        print("Extracting Data from HTML file")
    def parseData(self):
        print("Parsing Data from HTML file")
    def close(self):
        print("Closing File from HTML file\n\n") 

def DisplayContent(DisplayObj:DisplayContentTemplate):
        path = input("Please Enter File Path: ")
        DisplayObj.DisplayContent(path)

if __name__ == "__main__":
    print("MarkDown File")
    MdObj =  DisplayMDContent()
    DisplayContent(MdObj)

    print("HTML File")
    htmlObj =  DisplayHTMLContent()
    DisplayContent(htmlObj)