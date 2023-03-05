import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Bhuvnesh"
    return f"Hello,my name is {name}"

if __name__ == "__main__":
    app.run()
