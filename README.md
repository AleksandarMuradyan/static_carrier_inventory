# static_carrier_inventory

Requirements:
python
venv

Navinage to project folder and execute the following:

virtualenv venv
source venv/bin/activate
pip install flask

usage:

python carrier_inventory.py --request_status <completed/failed>
if run with 'carrier_inventory.py --request_status completed' -> will return a completed request status
if run with 'carrier_inventory.py --request_status failed' -> will return a failed request status

API URIs:

GET methods:
http://127.0.0.1:8000/locations
http://127.0.0.1:8000/products
http://127.0.0.1:8000/ports
http://127.0.0.1:8000/prices
http://127.0.0.1:8000/requests

POST methods:
http://127.0.0.1:8000/login
http://127.0.0.1:8000/locations_post
http://127.0.0.1:8000/ports_post
http://127.0.0.1:8000/connections_post
