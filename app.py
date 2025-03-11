#starting of the app
from flask import Flask,render_template

app=None

def setup_app():
  app=Flask(__name__)
  app.debug=True
  #Pending here is squilite conection
  app.app_context().push()#direct access to other modules
  print("ticket show app is started...")

#call the setup
setup_app()

from backend.controllers import *

if __name__=="__main__":
  app.run()