class Config:
    DATABASE_NAME = 'catalog_db'
    DATABASE_USER = 'anonymous_user'
    SQLALCHEMY_DATABASE_URI = 'mysql://counter:@localhost/catalog_db'

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}