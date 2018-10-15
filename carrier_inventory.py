from flask import Flask, jsonify, Response, request
import json
import os
import argparse

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def parseArguments():
    # Create argument parser
    #parser = argparse.ArgumentParser()
    #args = parser.parse_args()
    return args


@app.route('/api/locations', methods=['GET', 'POST'])
def locations():
    if request.method == 'POST':
        with open(os.path.join(basedir, 'locations_post_data.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')
    else:
        with open(os.path.join(basedir, 'locations_data.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')


@app.route('/api/products', methods=['GET'])
def products():
    with open(os.path.join(basedir, 'ports_data.json'), 'r') as f:
        return Response(f.read(), mimetype='application/json')


@app.route('/api/prices', methods=['GET'])
def prices():
    with open(os.path.join(basedir, 'ports_pricing_data.json'), 'r') as f:
        return Response(f.read(), mimetype='application/json')


@app.route('/api/ports', methods=['GET', 'POST'])
def ports():
    if request.method == 'GET':
        with open(os.path.join(basedir, 'ports_get.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')
    else:
        with open(os.path.join(basedir, 'ports_post_data.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')


@app.route('/api/requests/<int:_id>', methods=['GET', 'POST'])
def requests(_id):
    if args.request_status == "completed" and request.method == 'GET' and _id == 4662:
        with open(os.path.join(basedir, 'req_stat_4662.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')
    elif args.request_status == "completed" and request.method == 'GET' and _id == 4663:
        with open(os.path.join(basedir, 'req_stat_4663.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')
    elif args.request_status == "completed" and request.method == 'GET' and _id == '':
        with open(os.path.join(basedir, 'requests_status_completed.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')
    else:
        with open(os.path.join(basedir, 'requests_status_failed.json'), 'r') as f:
            return Response(f.read(), mimetype='application/json')


@app.route('/api/login', methods=['POST'])
def login():
    with open(os.path.join(basedir, 'login_post_data.json'), 'r') as f:
        return Response(f.read(), mimetype='application/json')

    # @app.route('post/api/login')
    # def login():
    #     json_data = request.get_json()
    #     email = json_data['email']
    #     password = json_data['password']
    #     return jsonify(token=generate_token(email, password))


@app.route('/api/connections', methods=['POST'])
def connections():
    with open(os.path.join(basedir, 'connections_post_data.json'), 'r') as f:
        return Response(f.read(), mimetype='application/json')


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
