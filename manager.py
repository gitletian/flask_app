# coding: utf-8
# __author__: ""
import os
from app import create_app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    app.run()
