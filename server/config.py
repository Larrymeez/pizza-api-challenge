import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///pizza.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
