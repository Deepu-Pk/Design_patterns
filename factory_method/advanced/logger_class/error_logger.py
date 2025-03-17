from iloger import ilogger 


class errorLogger(ilogger):
    def log(self, msg : str) -> None:
        print(f"[ERROR] : {msg}") 

    def __del__(self):
        pass