from desktop_builder import desktopBuilder 

class dellBuilder(desktopBuilder):
    def __init__(self):
        super().__init__()
        self._desktop.brand = "Dell"
    def buildMotherboard(self):
        self._desktop.motherboard = "Dell motherboard" 

    def buildProcessor(self):
        self._desktop.processor = "Dell procressor" 
    
    def buildMemory(self):
        self._desktop.memeory = "Dell memory" 

    def buildStograge(self):
        self._desktop.storage = "Dell storage" 

    def buildGraphicCard(self):
        self._desktop.graphic_card = "Dell Grahic card" 