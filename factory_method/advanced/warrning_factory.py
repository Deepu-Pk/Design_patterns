from iloger import ilogger
from warnnig_logger import warnnigLogger 
from logger_factory import loggerFactory

class warnnigFactory(loggerFactory):

    def createLogger(self):
        return warnnigLogger()