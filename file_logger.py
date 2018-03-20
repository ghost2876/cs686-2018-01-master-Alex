class file_logger:


    """
    Constructor
    """
    def __init__(self, log_level, filename = 'file_log.txt'):
        self.__log_level__ = log_level
        self.__f__ = open(filename, 'a+')
        #f.close()


    """
    log
    Logs the message if log_level is less than or equal to
    the class' threshold. (In this case: does nothing.)
    """
    def log(self, log_level, message):
        if (log_level <= self.__log_level__):
            self.__f__.write(str(log_level) + ": " + message + "\n")