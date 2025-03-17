# Load factory class
from error_factory import errorFactory 
from debug_factory import debugFactory 
from info_factory import infoFactory 
from warrning_factory import warnnigFactory 

# Load log classs
# from error_logger import errorLogger
# from debug_logger import debugLogger 
# from info_logger import infoLogger 
# from warnnig_logger import warnnigLogger 

if(__name__ == "__main__"):
    # Create error log
    error_log_ob = errorFactory()
    error_log = error_log_ob.createLogger()
    error_log.log("This is error message")

    # Create info log 
    info_log_ob = infoFactory()
    info_log = info_log_ob.createLogger() 
    info_log.log("This is info message")

    # Create debug log 
    debug_log_ob = debugFactory() 
    debug_log = debug_log_ob.createLogger() 
    debug_log.log("This is debug message")

    # Create wartnning message 
    warnnig_log_ob = warnnigFactory() 
    warnnig_log = warnnig_log_ob.createLogger() 
    warnnig_log.log("This is warnnig message")