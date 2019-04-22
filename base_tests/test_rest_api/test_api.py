import pytest

services = ['dog_api', 'openbrewerydb', 'cdnjs']
content_types_json = [
	"application/json",
	"application/json; charset=utf-8"
]
content_types_text = [
	'application/json',
	"text/html",
	"text/html; charset=utf-8"
]
SUCCESS = 200
FAIL = [200, 404, 503]
empty_data = [{}, {'test': 'fail'}]


def test_endpoint_response_status(client):
	response = client._get()
	assert response.status_code == SUCCESS


def test_endpoint_response_ok(client):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.ok is not False


def test_endpoint_responce_reason(client):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.reason == 'OK'


def test_endpoint_url(client):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.url == "/".join([client.address, client.endpoint])


def test_endpoint_content_type(client):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.headers['Content-type'] in content_types_json


@pytest.mark.parametrize("data", empty_data)
def test_negative_empty_post(client, data):
	r = client._post(data)
	assert r.status_code in FAIL
	assert str(r.headers['Content-type']).lower() in content_types_text
