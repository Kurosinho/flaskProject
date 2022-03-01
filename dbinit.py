from app import create_app
from app import db
import models

if __name__ == '__main__':
    db.create_all(app=create_app())
