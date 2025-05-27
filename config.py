import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config:
    HOST = '127.0.0.1'
    PORT = 5001
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///reservas.db"  # Exemplo usando SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento de modificações