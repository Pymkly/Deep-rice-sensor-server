import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'config.ini')

# Using INI configuration file
from configparser import ConfigParser

config = ConfigParser()
config.read(CONFIG_PATH)

HOST = str(config.get("POSTGRESQL", "HOST"))
DATABASE = str(config.get("POSTGRESQL", "DATABASE"))
USER = str(config.get("POSTGRESQL", "USER"))
PASSWORD = str(config.get("POSTGRESQL", "PASSWORD"))

MONGODB_DATABASE = str(config.get("MONGODB", "DATABASE"))
SENSOR_COLLECTION = str(config.get("MONGODB", "SENSOR_COLLECTION"))



