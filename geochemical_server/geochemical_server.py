from flask import Flask, request
import simulator

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    # Retrieve input data from the request
    values = request.json
    
    # Perform simulations using the input data
    results = simulator.simulate(values['data'])
    print(results)
    # Return simulation results as JS
    return results

if __name__ == '__main__':
    app.run(port=8000, debug=True)