"""
Base test for an array.
1. Check the array length.
2. Check the array has an element.
"""


def test_len(start_session, start_module, wrap_test):
	res = [x for x in range(6)]
	assert len(res) == 6


def test_a_in_b(wrap_test):
	res = [1, 2, 3]
	assert res[1] == 2
