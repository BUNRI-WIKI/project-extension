from loguru import logger

import socket

def InitializeLogger(cls):
    cls.init_static()
    return cls

@InitializeLogger
class Logger:
    def init_static() -> None:
        __sink = 'logfile.log'
        __format = '{time} - {extra[user]}:{extra[ip]} | {level} | {message}'
        __retention = '3 day'

        host = socket.gethostname()
        ip = socket.gethostbyname(host)

        logger.configure(extra={"user": host, "ip": ip})
        logger.remove()
        logger.add(
            sink=__sink, 
            format=__format,
            retention=__retention
        )

    @staticmethod
    def debug(msg) -> None:
        logger.debug(msg)
    
    @staticmethod
    def info(msg) -> None:
        logger.info(msg)

    @staticmethod
    def success(msg) -> None:
        logger.success(msg)
    
    @staticmethod
    def warning(msg) -> None:
        logger.warning(msg)
    
    @staticmethod
    def error(msg) -> None:
        logger.error(msg)
    