from application import app, db
from dotenv import load_dotenv
import os
load_dotenv()

def main():
    PORT=os.environ.get("PORT_DEV")
    DEBUG=os.environ.get("FLASK_DEBUG")
    HOST=os.environ.get("HOST_DEV")
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == "__main__":
    main()
    with app.app_context():
        app.run(debug=True)