from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr
    geo_response = requests.get(f'https://ipinfo.io/{client_ip}/json')
    location = geo_response.json().get('city', 'Lagos')
    print(location)
    response = {
        "client_ip": client_ip,
        "location": location, 
        "Greeting": f"Hello {visitor_name}"
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
