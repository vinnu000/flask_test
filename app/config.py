import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    """
    Security secret key
    """
    SECRET_KEY = "This is an UNSECURE Secret. CHANGE THIS for production environments."


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-dev.db".format(base_dir)
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-dev.db".format(base_dir)
    TESTING = True


class ProductionConfig(BaseConfig):
    CONFIG_NAME = "prod"
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///{0}/app-dev.db".format(base_dir)
    TESTING = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
