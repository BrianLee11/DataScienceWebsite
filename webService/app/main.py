import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template
import webbrowser
import threading

# Import route registration function
from routes.register_routes import register_routes

# Initialize Flask app
app = Flask(__name__)
integer = 2

# Register routes from the home_routes module
register_routes(app)

# main.py
# import tests
from tests.simpleLinearRegression2D import simpleData2D
x_coordinates = [cordinate[0] for cordinate in simpleData2D]

from services.linearRegression import simpleLinearRegression, simpleLinearPredict
estimates = simpleLinearRegression(simpleData2D)
predicted = simpleLinearPredict(estimates[0], estimates[1], x_coordinates)

from services.plotGraph import plot2DGraph
img_bytes = plot2DGraph(simpleData2D, show_plot=True)  # show and return

from internalFunctions.logic import add_integer

import base64

@app.route('/linearRegression')
def linearRegression():
    result_integer = add_integer('linearRegression')

    # Base64 encode the image for HTML embedding
    graph_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

    return render_template('linearRegression.html', integer=result_integer, graph=graph_base64)



# Open browser
def open_browser():
    try:
        webbrowser.open_new('http://127.0.0.1:5000')
    except Exception as e:
        print(f"Could not open browser: {e}")

if __name__ == '__main__':
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True)
