"""
test The stack functions
"""
import stack as stack
import unittest

class TestStackMethods(unittest.TestCase):
    """yes
    """

    def test_isOnlyElement(self):
        s = stack.Stack()
        self.assertTrue(s.isOnlyElement())

    def test_push(self):
        s = stack.Stack()
        s.push(3)
        self.assertEqual(s.top.data, 3)

if __name__ == '__main__':
    unittest.main()
