from flask_frozen import Freezer
from app import app  # Ensure this matches the name of your Flask app file (app.py)

freezer = Freezer(app)

if __name__ == "__main__":
    freezer.freeze()

