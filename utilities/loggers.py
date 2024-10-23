import logging
import inspect

class LoggingClass:

    @staticmethod
    def log_generator():
        insert_names = inspect.stack()[1][3]
        logger = logging.getLogger(insert_names)
        logfile = logging.FileHandler('D:\\Peettam\\MySiteBook\\Logs\\log_msb')
        file_format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(message)s")
        logfile.setFormatter(file_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
