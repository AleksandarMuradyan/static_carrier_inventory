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
http://127.0.0.1:8000/api/locations
http://127.0.0.1:8000/api/products
http://127.0.0.1:8000/api/ports
http://127.0.0.1:8000/api/prices
http://127.0.0.1:8000/api/requests

POST methods:
http://127.0.0.1:8000/api/login
http://127.0.0.1:8000/api/locations
http://127.0.0.1:8000/api/ports
http://127.0.0.1:8000/api/connections
