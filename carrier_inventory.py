from flask import Flask, jsonify, request
import os
import argparse

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def parseArguments():
    # Create argument parser
    #parser = argparse.ArgumentParser()
    parser.add_argument("--RequestStatus", help="completed/failed", type=str)
    args = parser.parse_args()
    return args


@app.route('/locations', methods=['GET'])
def locations():
    with open(os.path.join(basedir, 'locations_data.json'), 'r') as f:
        return f.read()


@app.route('/products', methods=['GET'])
def products():
    with open(os.path.join(basedir, 'ports_data.json'), 'r') as f:
        return f.read()


@app.route('/prices', methods=['GET'])
def prices():
    with open(os.path.join(basedir, 'ports_pricing_data.json'), 'r') as f:
        return f.read()


@app.route('/ports', methods=['GET'])
def ports():
    with open(os.path.join(basedir, 'port_spec_data.json'), 'r') as f:
        return f.read()


@app.route('/requests', methods=['GET'])
def requests():
    if args.request_status == "completed":
        with open(os.path.join(basedir, 'requests_status_completed.json'), 'r') as f:
            return f.read()
    else:
        with open(os.path.join(basedir, 'requests_status_failed.json'), 'r') as f:
            return f.read()


@app.route('/login', methods=['POST'])
def login_post():
    with open(os.path.join(basedir, 'login_post_data.json'), 'r') as f:
        return f.read()


@app.route('/locations_post', methods=['POST'])
def locations_post():
    with open(os.path.join(basedir, 'locations_post_data.json'), 'r') as f:
        return f.read()

@app.route('/ports_post', methods=['POST'])
def ports_post():
    with open(os.path.join(basedir, 'ports_post_data.json'), 'r') as f:
        return f.read()
    # return jsonify(
    #     {
    #         "price_id": "89",
    #         "location_id": "543",
    #         "port_name": "LexCorp Port"
    #     })


@app.route('/connections_post', methods=['POST'])
def connections_post():
    with open(os.path.join(basedir, 'connections_post_data.json'), 'r') as f:
        return f.read()

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--request_status", help="completed/failed", type=str)
    args = parser.parse_args()
    if args.request_status:
        print(args.request_status)
    print("You are running the script with arguments: ")
    for a in args.__dict__:
        print(str(a) + ": " + str(args.__dict__[a]))


    # Set up the development server on port 8000.
    app.run(host='0.0.0.0', port=8000, debug=True)