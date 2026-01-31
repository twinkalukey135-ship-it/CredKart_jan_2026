import logging


class log_generator_class: #created the class to generate and return logger object
    @staticmethod #without creating the class object
    def log_gen_method(): #method and will return logger
        log_file = logging.FileHandler(".\\Logs\\CredKart.logs") #log file
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funName)s - %(lineno)d - %(message)s') # log format
        log_file.setFormatter(log_format) # log file --> log format (applying the format to log file)
        logger = logging.getLogger() # #get logger object
        logger.addHandler(log_file) # add new log everytime in same log file
        logger.setLevel(logging.INFO) # level set
        return logger


"""
log level : 

debug
info
warning
error
critical

"""



