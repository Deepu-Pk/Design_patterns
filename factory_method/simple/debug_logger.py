from ilogger import ilogger

class debugLogger(ilogger):
    def  log(self, string : str) -> None:
        print(f"[DUBUG] : {string}")

    def __del__(self) -> None:
        pass 