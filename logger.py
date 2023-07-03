import logging

class Logger:
    """
    Classe Logger para facilitar a criação de logs.

    Atributos
    ---------
    logger_name : str
        Nome do logger.
    level : int, opcional
        Nível de log (por padrão, logging.INFO).
    format : str, opcional
        Formato das mensagens de log (default é '%(asctime)s - %(name)s - %(levelname)s - %(message)s').
    log_file : str, opcional
        Nome do arquivo de log (por padrão, None).

    Métodos
    -------
    log(message, level):
        Cria um registro de log com a mensagem e o nível especificados.
    """

    def __init__(self, logger_name, level=logging.DEBUG, 
                 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                 log_file=None):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(format)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        else:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    def log(self, message, level):
        """
        Cria um registro de log.

        Parâmetros
        ----------
        message : str
            A mensagem a ser logada.
        level : str
            O nível do log. Deve ser um dos seguintes: 'info', 'debug', 'warning', 'error', 'critical'.
        """
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'critical':
            self.logger.critical(message)
