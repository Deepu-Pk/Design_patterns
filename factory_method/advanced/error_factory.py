from iloger import ilogger 
from logger_factory import loggerFactory
from error_logger import errorLogger

class errorFactory(loggerFactory):


    def createLogger(self) -> ilogger:
        return errorLogger()