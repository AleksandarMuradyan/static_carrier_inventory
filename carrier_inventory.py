from flask import Flask
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/locations', methods = ['GET'])
def locations():
    with open(os.path.join(basedir, 'locations_data.json'), 'r') as f:
        return f.read()

@app.route('/ports', methods = ['GET'])
def ports():
    with open(os.path.join(basedir, 'ports_data.json'), 'r') as f:
        return f.read()

@app.route('/port_spec', methods = ['GET'])
def port_spec():
    with open(os.path.join(basedir, 'port_spec_data.json'), 'r') as f:
        return f.read()

if __name__ == "__main__":
    port = 8000
    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}/".format(port))
    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)