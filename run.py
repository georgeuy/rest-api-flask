from application import create_app, db
from application import models

from flask_migrate import Migrate



app = create_app()

Migrate(app, db)

if __name__ == "__main__":
    app.run(port=3000, debug=True)