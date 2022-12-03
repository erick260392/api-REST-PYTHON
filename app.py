from flask import Flask, request
from flask_api import status
from abilitys import ability
from flask import  jsonify

app = Flask(__name__)

@app.route('/ability', methods=["GET"])
def getability():
    
    
    return jsonify(ability["ability"]["name"])
    


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000, debug=True)