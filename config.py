class Config:
    SECRET_KEY = 'this1is2a3secret4key6that7no8one9should0know1because4if5not6they7will8hack9my1soul'
    DATABASE_NAME = 'catalog_db'
    DATABASE_USER = 'anonymous_user'
    SQLALCHEMY_DATABASE_URI = 'mysql://counter:@localhost/catalog_db'
    PROPAGATE_EXCEPTIONS = True
    ERROR_404_HELP = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}