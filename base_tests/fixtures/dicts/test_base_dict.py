"""
Base test for the dict.
1. Check the dict has a key.
2. Check the dict has a value.
"""


def test_key(wrap_test, test_dict):
	assert 'a' in test_dict.keys()


def test_value(wrap_test, test_dict):
	assert 2 in test_dict.values()
