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

services = ['dog_api', 'openbrewerydb', 'cdnjs']

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


def pytest_addoption(parser):
	parser.addoption(
		"--service", action="store"
	)
	parser.addoption(
		"--all-services", action='store_true'
	)


@pytest.fixture
def client(request):
	if request.config.option.service:
		if request.config.option.service not in services:
			pytest.exit('service name not in {}'.format(services))
		return APIClient(request.config.getoption("service"))
	elif request.config.option.all_services:
		for service in services:
			return APIClient(service)
	else:
		raise pytest.exit(
			'\nif you want to run tests fot specific service'
			' use --service {dog_api|openbrewerydb|cdnjs},'
			'\nor use --all-services if you want to run tests for all services')
