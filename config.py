import os


class Config:
    '''
    Parent configuration class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json (Links to an external site.)'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7166@localhost/blogs'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: takes the parent configuration class as an argument
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    '''
    Child configuration class
    Args:
        Config:takes the configuration child class as an argument 
    '''

    DEBUG = True


config_options={
    'development':DevConfig,
    'production':ProdConfig
}