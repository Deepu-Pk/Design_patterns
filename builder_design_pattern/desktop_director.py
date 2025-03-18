from dell_builder import dellBuilder 
from hp_builder import HpBuilder 
from desktop_builder import desktopBuilder

class desktopDirector():
    def buildDesktop(self,builder : desktopBuilder):
        builder.buildMotherboard() 
        builder.buildProcessor() 
        builder.buildMemory()
        builder.buildStograge() 
        builder.buildGraphicCard()
        return builder.getDesktop()
    
