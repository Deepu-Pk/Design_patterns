from iloger import ilogger


class debugLogger(ilogger):
    def log(self, msg : str) -> None:
        print(f"[DEBUG] : {msg}")

    def __del__(self):
        pass