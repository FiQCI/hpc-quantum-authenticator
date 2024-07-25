import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET = os.getenv("SECRET")
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    HELMI_URL = os.getenv("DEV_HELMI_URL")
class ProductionConfig(Config):
    HELMI_URL = os.getenv("PROD_HELMI_URL")

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True