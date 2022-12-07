from flask import Flask, request
import requests

app = Flask(__name__)

def controller_poke(headers):
    try:
      end_point_poke_Api = headers['end_point_poke_Api']
      exits_ability_name = headers['ability_name']
      ability_range = headers['ability_range']
      
      ability_range = int(ability_range)
      
      response = requests.get(end_point_poke_Api)
      #print(response.status_code)
      response = response.json()
   
       # print(response)
    
      abilities = response['abilities'][ability_range]
      ability_name = abilities['ability']['name']

      print(abilities,ability_name)
    except Exception as e:
         return {'error':e.args[0]} , 400
    else:
        if exits_ability_name in ability_name:
            return {'exist_ability_name':True},200
        return {'exist_ability_name':False},200
                
 
   

@app.route('/poke')
def poke():
        response = controller_poke(request.headers)
        return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000, debug=True)
