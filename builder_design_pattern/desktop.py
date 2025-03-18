
# Desktop class
class Desktop:
    def __init__(self):
        self.brand = ""
        self.motherboard = ""
        self.processor = "" 
        self.memeory = ""
        self.storage = ""
        self.graphic_card = ""
    

    def display(self) -> None: 
        print(f"== {self.brand} details ==")
        print(f"Motherboard : {self.motherboard}")
        print(f"Processor : {self.processor}")
        print(f"Memory : {self.memeory}")
        print(f"Storage : {self.storage}")
        print(f"Graphic card : {self.graphic_card}") 

