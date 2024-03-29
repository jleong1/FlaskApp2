from flask import Flask
 
app = Flask(__name__)
 
app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'your-username@gmail.com'
app.config["MAIL_PASSWORD"] = 'your-password'
 
from routes import mail
mail.init_app(app)
 
import FeelsApp.routes