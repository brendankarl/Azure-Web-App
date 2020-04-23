import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Brendan Griffin"

if __name__ == "__main__":
    app.run()