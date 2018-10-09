import json
import pytest
from carrier_inventory import app

# GET methods:
url = 'http://127.0.0.1:8000/get/api/locations'
url1 = 'http://127.0.0.1:8000/get/api/locations'
url2 = 'http://127.0.0.1:8000/get/api/products'
url3 = 'http://127.0.0.1:8000/get/api/ports'
url4 = 'http://127.0.0.1:8000/get/api/prices'
url5 = 'http://127.0.0.1:8000/get/api/requests'

# POST methods:
url6 = 'http://127.0.0.1:8000/post/api/login'
url7 = 'http://127.0.0.1:8000/post/api/locations'
url8 = 'http://127.0.0.1:8000/post/api/ports'
url9 = 'http://127.0.0.1:8000/post/api/connections'


@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client


def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def json_of_response(response):
    """Decode json from response"""
    return json.loads(response.data.decode('utf8'))


def test_locations(client):
    response = client.get(url1)
    assert response.status_code == 200
    assert b'UK_TEST_01' in response.data
    assert b'customer_site_name' in response.data
    assert "UK_TEST_01" in str(response.data)


def test_products(client):
    response = client.get(url2)
    assert response.status_code == 200
    assert b'"service_type":"ETHERNETPORT"' in response.data
    assert b'ports_available' in response.data


def test_ports_spec(client):
    response = client.get(url3)
    assert response.status_code == 200
    assert b'"connector":	"RJ45"' in response.data
    assert b'bandwidth' in response.data
    assert b'port_id' in response.data


def test_prices(client):
    response = client.get(url4)
    assert response.status_code == 200
    assert b'"rental_unit"' in response.data
    assert b'installation_charge' in response.data
    assert b'installation_currency' in response.data


# def test_requests(client):
#     response = client.get(url5)
#     assert response.status_code == 200
#     assert b'"requested_at"' in response.data


def test_login(client):
    response = post_json(client, url6, {'key': 'value'})
    assert response.status_code == 200
    assert json_of_response(response) == {"token": "string"}


def test_locations_post(client):
    response = post_json(client, url7, {"site_id": "2"})
    assert response.status_code == 200
    assert json_of_response(response) == {'customer_location_list': [{'customer_site_name': 'Headquarters',
                                       'site_id': '2'},
                                      {'customer_site_name': 'LexCorp Head Office',
                                       'site_id': '543'}]}


def test_ports_post(client):
    response = post_json(client, url8, {"site_id": "2"})
    assert response.status_code == 200
    assert 'response_url' in json_of_response(response)


def test_conn_post(client):
    response = post_json(client, url9, {"price_id": "10"})
    assert response.status_code == 200
    assert json_of_response(response) == {
                                            "price_id": "10",
                                            "connection_name": "My test connection",
                                            "component_connections": [
                                                {
                                                    "from_port_id": "80000121",
                                                    "to_port_id": "80000117",
                                                    "a_end_vlan_mapping": "FM",
                                                    "b_end_vlan_mapping": "X",
                                                    "a_end_vlan_type": "C",
                                                    "b_end_vlan_type": "C",
                                                    "a_end_vlan_ids": [
                                                        {
                                                            "from_id_range": 1,
                                                            "to_id_range": 1
                                                        },
                                                        {
                                                            "from_id_range": 5,
                                                            "to_id_range": 10
                                                        }
                                                    ],
                                                    "b_end_vlan_ids": [
                                                        {
                                                            "from_id_range": 5,
                                                            "to_id_range": 5
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
    assert "from_port_id" in str(response.data)


# def test_products_api(client):
#     response = client.get('http://127.0.0.1:8000/get/api/products')
#     with open(os.path.join(basedir, 'ports_data.json'), 'r') as f:
#         assert response.json in json.loads(f.read())
#
#
# def test_ports_api(client):
#     response = client.get('http://127.0.0.1:8000/get/api/ports')
#     # = os.path.join(basedir, 'port_spec_data.json')
#
#     with open(os.path.join(basedir, 'ports_data.json'), 'r') as f:
#         json_data = json.loads(f.read())
#         assert response.json == json_data
#         print(json_data)
#         y = response.json
#         print(y)
#         #assert os.path.join(basedir, 'port_spec_data.json') in response.json
