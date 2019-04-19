import pytest
import requests
from collections import namedtuple

ApiType = namedtuple('ApiType', ['url', 'endpoint'])
API_URL = {
	'dog_api': ApiType(
		'https://dog.ceo', 'api/breeds/list/all'
	),
	'openbrewerydb': ApiType(
		'https://api.openbrewerydb.org', 'breweries?by_state'
	),
	'cdnjs': ApiType(
		'https://api.cdnjs.com', 'libraries/api-check'
	),
}


class APIClient:
	def __init__(self, service):
		self.address = API_URL[service].url
		self.endpoint = API_URL[service].endpoint

	def _get(self):
		url = "/".join([self.address, self.endpoint])
		return requests.get(url)

	def _post(self, data):
		url = "/".join([self.address, self.endpoint])
		return requests.post(url, json=data)


@pytest.fixture
def client(service):
	return APIClient(service)
