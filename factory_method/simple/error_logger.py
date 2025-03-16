from ilogger import ilogger 


class errorLogger(ilogger):
    def log(self, string : str):
        print(f"[ERROR] : {string}")

    def __del__(self) -> None:
        pass 