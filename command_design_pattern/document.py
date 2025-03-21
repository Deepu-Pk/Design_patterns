"""
    Implementation of commanda design pattern 
    Example document saving and opening 
"""

from abc import ABC,abstractmethod 

# Command interface
class Command(ABC):

    @abstractmethod
    def excute(self):
        pass 


# Document 
class Document:
    def open(self):
        print(f"Document is opened") 
    
    def save(self):
        print(f"Document is saved") 


# Concreate command for docuement open 
class documentOpen(Command):
    def __init__(self,document : Document):
        self.__document = document 

    def excute(self):
        self.__document.open() 


# Concreate command for save the document 
class documentSave(Command):
    def __init__(self,document : Document):
        self.__document = document 

    def excute(self):
        self.__document.save()
 


# Command invoker 

class Invoker:
    def __init__(self):
        self.__commands : list = [] 

    def addCommand(self,commad : Command):
        self.__commands.append(commad) 

    def excuteCommand(self):
        for command in self.__commands:
            command.excute() 

    

def main():
    document = Document() 
    invoker = Invoker()

    click_open = documentOpen(document)
    click_save = documentSave(document) 

    invoker.addCommand(click_open)
    invoker.addCommand(click_save) 

    invoker.excuteCommand()

if(__name__ == "__main__"):
    main()

