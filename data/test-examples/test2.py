import unittest

class MyTest(unittest.TestCase):

    def test_fail(self):
        x = 'This is local'
        y = 1+1
        assert y == 2
        assert False
#         if not False:
#             raise AssertionError

    def test_fail_message(self):
        assert False, 'This is an assértion message'
#         if not False:
#             raise AssertionError('This is an assértion message')

    def test_math(self):
        assert 1 + 1 == 2, 'Math is broken'
