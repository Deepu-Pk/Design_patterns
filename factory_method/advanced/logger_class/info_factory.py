from iloger import ilogger
from logger_factory import loggerFactory 
from info_logger import infoLogger 



class infoFactory(loggerFactory):

    def createLogger(self) -> ilogger:
        return infoLogger()