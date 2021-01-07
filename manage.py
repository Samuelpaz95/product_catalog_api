from flask_script import Manager
from app import create_app
from config import config

APP = create_app(config=config['development'])
MANAGER = Manager(APP)
if __name__ == "__main__":
    MANAGER.run()