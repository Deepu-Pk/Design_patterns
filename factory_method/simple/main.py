from logger_factory import createLogger 
from ilogger import ilogger



if(__name__ == "__main__"):
    error_log : ilogger = createLogger("ERROR") 
    info_log : ilogger = createLogger("INFO") 
    debug_log : ilogger = createLogger("DEBUG")
    warnnig_log : ilogger = createLogger("WARNNIG")

    error_log.log("This is error message")
    info_log.log("This is information message") 
    debug_log.log("This is debug message")
    warnnig_log.log("This is warnnig message")