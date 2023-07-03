from logger import Logger
def test_logger():
    logger = Logger('test_logger', log_file='test_logger.log')
    logger.log('Testando logger', 'info')
    logger.log('Testando logger', 'debug')
    logger.log('Testando logger', 'warning')
    logger.log('Testando logger', 'error')
    logger.log('Testando logger', 'critical')


test_logger()