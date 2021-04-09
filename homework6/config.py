import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "sqlite:///:memory:")
    APP_PORT = os.environ.get("APP_PORT", "8080")
    APP_DEBUG = os.environ.get("APP_DEBUG", "1") == '1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
