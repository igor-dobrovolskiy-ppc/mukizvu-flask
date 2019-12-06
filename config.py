class Config(object): 
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config): 
    pass 


class DevConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///mukizvu.db"
    SQLALCHEMY_ECHO = True
