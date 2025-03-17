from iloger import ilogger

class warnnigLogger(ilogger):

    def log(self, msg : str) -> None:
        print(f"[WARNNIG] : {msg}") 

    def __del__(self):
        pass