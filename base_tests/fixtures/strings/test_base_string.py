"""
base test for strings
1. Check two strings concatenation.
2. Check the string length.
"""


def test_concat_a_b(wrap_test):
	assert 'aaa' + 'bbb' == 'aaabbb'


def test_len(wrap_test, test_string):
	assert len(test_string) == 10
