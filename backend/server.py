from flask import Flask
from flask_cors import CORS

app = Flask(__name__) # create a Flask app
CORS(app)


@app.route('/get_route')
def get_route():
    return 'Hello, World!'


if __name__ == '__main__': 
    app.run() # run our Flask app default on localhost:5000