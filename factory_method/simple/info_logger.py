from ilogger import ilogger 


class infoError(ilogger):
    def log(self, string : str) -> None:
        print(f"[INFO] : {string}")
    def __del__(self) -> None:
        pass 