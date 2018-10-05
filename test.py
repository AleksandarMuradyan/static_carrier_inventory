import pytest
from flask import request
import os
from carrier_inventory import app


basedir = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client


def test_locations_api(client):
    response = client.get('http://localhost:8000/locations')
    client.assertEqual(response.json(), os.path.join(basedir, 'locations_data.json'))


def test_products_api(client):
    response = client.get('http://localhost:8000/products')
    assert response == (os.path.join(basedir, 'ports_data.json'))


def test_prices_api(client):
    response = client.get('http://localhost:8000/prices')
    client.assertEqual(response.json(), os.path.join(basedir, 'ports_pricing_data.json'))


def test_ports_api(client):
    response = client.get('http://localhost:8000/ports')
    client.assertEqual(response.json(), os.path.join(basedir, 'port_spec_data.json'))


#    self.assertEqual(response.json(), {'hello': 'world'})
#    self.assertEqual(response.json(), {'hello': 'world'})
#    client.assertEqual(response.json(), os.path.join(basedir, 'ports_data.json'))
#    self.assertEqual(response.json(), {'hello': 'world'})
#    self.assertEqual(response.json(), {'hello': 'world'})
