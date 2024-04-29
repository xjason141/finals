#example custom logger with a 'debug' and StreamHandler
import logging

#create logger
stream_logger = logging.getLogger('stream_logger')
stream_logger.setLevel(logging.DEBUG) #set logger to capture all messages from DEBUG level and above

#ensure no previous handlers are attached
stream_logger.handlers = []

#create StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO) #set handler to display only messages from INFO level and above

#add handler to logger
stream_logger.addHandler(stream_handler)

#logging messages at diff levels
stream_logger.debug('This is a DEBUG message for strea_logger.')
stream_logger.info('This is a INFO message for strea_logger.')
stream_logger.warning('This is a WARNING message for strea_logger.')
stream_logger.error('This is a ERROR message for strea_logger.')
stream_logger.critical('This is a CRITICAL message for strea_logger.')
