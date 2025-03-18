from desktop_builder import desktopBuilder 

class HpBuilder(desktopBuilder):
    def __init__(self):
        super().__init__()
        self._desktop.brand = "Hp"
    def buildMotherboard(self):
        self._desktop.motherboard = "Hp motherboard" 

    def buildProcessor(self):
        self._desktop.processor = "Hp procressor" 
    
    def buildMemory(self):
        self._desktop.memeory = "Hp memory" 

    def buildStograge(self):
        self._desktop.storage = "Hp storage" 

    def buildGraphicCard(self):
        self._desktop.graphic_card = "Hp Grahic card" 