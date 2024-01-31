from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, static_folder='static')

CFD_SIMULATOR_URL = 'http://127.0.0.1:8080'
GEOCHEMICAL_SIMULATOR_URL = 'http://127.0.0.1:8000'


# define a route to serve the home.html file
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/temperatura_simulator')
def temperatura_simulator():
    return render_template('temperature_simulator.html')

@app.route('/geochemical_simulator')
def geochemical_simulator():
    return render_template('geochemical_simulator.html')



# define a route to trigger the simulation
@app.route('/GeochemicalSimulationProxy', methods=['POST'])
def GeochemicalSimulationProxy():
    # get any parameters needed for the simulation from the request
    # call your simulation function with the parameters and get the results
    data = request.json

    # Send a request to the simulator microservice
    response = requests.post(f'{GEOCHEMICAL_SIMULATOR_URL}/simulate', json={"data": data})
    
    print(response.json())
    if response.status_code == 200:
        simulation_results = response.json()
        return jsonify(simulation_results)
    else:
        return "Error communicating with the Geochemical simulator."



# define a route to trigger the simulation
@app.route('/CFDSimulationProxy', methods=['POST'])
def CFDSimulationProxy():
    # get any parameters needed for the simulation from the request
    # call your simulation function with the parameters and get the results
    data = request.json
    #results = simulator.simulate(data)

    # Send a request to the simulator microservice
    response = requests.post(f'{CFD_SIMULATOR_URL}/simulate', json={"data": data})
    
    if response.status_code == 200:
        simulation_results = response.json()
        return jsonify(simulation_results)
    else:
        return "Error communicating with the CFD simulator."

if __name__ == '__main__':
    app.run(debug=True)
