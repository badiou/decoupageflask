# ici c'est app.py

from flask_migrate import Migrate
from models import db,app,Etudiant
migrate = Migrate(app, db)


@app.route('/', methods=['GET'])
def home():
    return 'Bonjour'


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)