import logging

# Set the minimum logging level to INFO,
logging.basicConfig(level=logging.INFO)

# Get a logger object
log = logging.getLogger('simple')

# Start the log file
log.info('Hello World')