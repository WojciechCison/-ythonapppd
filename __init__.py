from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
CORS(app, origins=['https://frontedncoctail.azurewebsites.net'])
import FlaskAPI.views