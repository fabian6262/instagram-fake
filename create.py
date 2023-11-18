from application import app, db
from application.model import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()