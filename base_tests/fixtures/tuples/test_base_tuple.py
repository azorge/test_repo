"""
Base test for the tuple.
1. Check element by index in tuple.
2. Check tuple length.
"""


def test_a_in_b(wrap_test, test_tuple):
	assert test_tuple[1] == 'two'


def test_len(wrap_test, test_tuple):
	assert len(test_tuple) == 3
