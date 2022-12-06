from flask import Flask, request
import requests


app = Flask(__name__)


def controller_poke(headers):
    try:
      end_point_poke_Api = headers['end_point_poke_Api']
      ability_name = headers['ability_name']
      
      response = requests.get(end_point_poke_Api)
      #print(response.status_code)
      response = response.json()
      print(response)
       # print(response)
       
       
      abilities = response['abilities'][0]
      ability_name = abilities['ability'][ 'name']

      print(abilities,ability_name)
    except:
        ...
    else:
        if 'static' in ability_name:
             print('Y')
        else:
            print('N')
                
 
    return {'controller_poke': True}

@app.route('/poke')
def poke():
        response = controller_poke(request.headers)
        return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000, debug=True)
