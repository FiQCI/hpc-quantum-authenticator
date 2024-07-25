import logging
from logging.handlers import RotatingFileHandler


def create_logger():
    """
    Customizes the default logger for the application.

    The logger outputs to both the console and a rotating file handler.
    The log format includes the timestamp, logger name, log level, and message.

    Returns:
        logging.Logger: Configured logger for the application.
    """
    logger = logging.getLogger('Quantum_logger')
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=3)
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    logging.getLogger('Quantum_logger').setLevel(logging.DEBUG)
    logging.getLogger('Quantum_logger').addHandler(console_handler)
    logging.getLogger('Quantum_logger').addHandler(file_handler)
    
    return logger
