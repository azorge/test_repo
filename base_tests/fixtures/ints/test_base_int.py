"""
Base test for ints.
1. Check sum of two ints.
2. Negative check for multiply of two ints.
"""


def test_sum_5_7(wrap_test):
	assert 5 + 7 == 12


def test_negative_mult_3_8(wrap_test):
	assert not 3 * 8 == 9000
