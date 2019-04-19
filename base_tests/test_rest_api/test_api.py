import pytest

services = ['dog_api', 'openbrewerydb', 'cdnjs']
content_types_json = ["application/json", "application/json; charset=utf-8"]
content_types_text = ["text/html", "text/html; charset=utf-8"]
SUCCESS = 200
FAIL = [404, 503]
empty_data = [{}, {'test': 'fail'}]


@pytest.mark.parametrize("service", services)
def test_endpoint_response_status(client, service):
	response = client._get()
	assert response.status_code == SUCCESS


@pytest.mark.parametrize("service", services)
def test_endpoint_response_ok(client, service):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.ok is not False


@pytest.mark.parametrize("service", services)
def test_endpoint_responce_reason(client, service):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.reason == 'OK'


@pytest.mark.parametrize("service", services)
def test_endpoint_url(client, service):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.url == "/".join([client.address, client.endpoint])


@pytest.mark.parametrize("service", services)
def test_endpoint_content_type(client, service):
	response = client._get()
	assert response.status_code == SUCCESS
	assert response.headers['Content-type'] in content_types_json


@pytest.mark.parametrize("service", services)
@pytest.mark.parametrize("data", empty_data)
def test_negative__post(client, service, data):
	r = client._post(data)
	assert r.status_code in FAIL
	assert str(r.headers['Content-type']).lower() in content_types_text
