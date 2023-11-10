import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'skhjdf97980909080997'