from ilogger import ilogger
from info_logger import infoError 
from error_logger import errorLogger 
from warrning_logger import warnnigLogger 
from debug_logger import debugLogger



def createLogger(p_logger : str):
    logger =  {
        "INFO" : infoError,
        "WARNNIG" : warnnigLogger, 
        "DEBUG" : debugLogger,
        "ERROR" : errorLogger
    }

    return logger[p_logger]() 