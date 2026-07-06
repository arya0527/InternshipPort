from flask import Flask
from flask_cors import CORS
from config import Config
from database import mysql

from routes.auth_routes import auth_bp
from routes.internship_routes import internship_bp
from routes.recommendation_routes import recommendation_bp
from routes.resume_routes import (
    resume_bp
)


app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*"}})

mysql.init_app(app)
@app.route("/")
def home():
    return {"message": "Backend running successfully"}

app.register_blueprint(auth_bp)
app.register_blueprint(internship_bp)
app.register_blueprint(recommendation_bp, url_prefix="/recommend")
app.register_blueprint(
    resume_bp
)
if __name__ == '__main__':
    app.run(debug=True)

