from ilogger import ilogger 


class warnnigLogger(ilogger):
    def log(self, string : str) -> None:
        print(f"[WARNNIG] : {string}")

    def __del__(self) -> None:
        pass 