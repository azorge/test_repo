import pytest

SEPARATOR = '=' * 6
RES_DICT = {'a': 1, 'b': 2}


def wrap_msg(msg):
	print('\n' + SEPARATOR + msg + SEPARATOR)


@pytest.fixture(scope="function")
def wrap_test(request):
	wrap_msg(' start test "{}" '.format(request.function.__name__))

	def end():
		wrap_msg(' end test ')

	request.addfinalizer(end)


@pytest.fixture(scope="module")
def start_module(request):
	wrap_msg(' start module ')

	def end():
		wrap_msg(' end module ')

	request.addfinalizer(end)


@pytest.fixture(scope="session")
def start_session(request):
	wrap_msg(' start session ')

	def end():
		wrap_msg(' end session ')

	request.addfinalizer(end)


@pytest.fixture(scope="module")
def test_dict():
	return RES_DICT


@pytest.fixture(scope="function")
def test_string():
	return 'teststring'


@pytest.fixture(scope="function")
def test_tuple():
	return 'one', 'two', 'three'
