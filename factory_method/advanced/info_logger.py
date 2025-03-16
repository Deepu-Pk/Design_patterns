from iloger import ilogger 



class infoLogger(ilogger):
    def log(self, msg : str) -> None:
        print(f"[INFO] : {msg}")

    def __del__(self):
        pass