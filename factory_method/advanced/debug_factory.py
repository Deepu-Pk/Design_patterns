from logger_factory import loggerFactory 
from iloger import ilogger 
from debug_logger import debugLogger 



class debugFactory(loggerFactory):

    def createLogger(self):
        return debugLogger()