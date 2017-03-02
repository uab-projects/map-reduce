"""
Allows to enable the Python logging system
"""
# Load default configuration
import logging
import logging.config

# Constants
CONFIG_FILE = "config/logging.conf"
"""
    str: default configuration file for logging
"""


# Load config
def init():
    """
    Initializes the logger with the default configuration
    """
    logging.config.fileConfig(CONFIG_FILE)
