import CoreSpark as cs
import unittest

class TestStringMethods(unittest.TestCase):

    def test_Map(self):
      self.assertEqual(cs.parallelize([1,2,3,4,5]).Map(lambda x:x*2).collect(), [2,4,6,8,10])

    def test_map2(self):
         self.assertEqual(cs.parallelize(map(lambda x:x*2,[1,2,3,4,5])).collect(), [2,4,6,8,10])

    def test_countByKey(self):
        self.assertEqual(cs.parallelize([("a", 1), ("b", 1), ("a", 1)]).countByKey(), {"b":1, "a":2})

    def test_keyBy(self):
        self.assertEqual(cs.parallelize([1,2,3]).keyBy(lambda x:x*2).collect(), [(2,1),(4,2),(6,3)])

    def test_reduce(self):
        self.assertEqual(cs.parallelize([1,2,3,4,5]).Reduce(lambda a,b: a + b), 15)

    def test_reduceTuple(self):
        self.assertEqual(cs.parallelize((1,2,3,4,5)).Reduce(lambda a,b: a + b), 15)

    def test_reduceMultiplication(self):
        self.assertEqual(cs.parallelize([1,2,3,4,5]).Reduce(lambda a,b: a * b), 120)

    def test_DicitonaryCollect(self):
        self.assertEqual(sorted(cs.parallelize({'jack': 4098, 'sape': 4139}).collect()), [('jack',4098), ('sape', 4139)])

    def test_DicitonaryCollect(self):
        self.assertEqual(sorted(cs.parallelize({'a': 1, 'b': 2}).collect()), [('a',1), ('b', 2)])

    def test_Dicitonary(self):
        self.assertEqual(cs.parallelize(["b", "a", "c"]).Map(lambda x: (x, 1)).collect(),[('b', 1), ('a', 1), ('c', 1)])

    def test_collect(self):
        self.assertEqual(cs.parallelize((1,2,3)).collect(), [1,2,3])



if __name__ == '__main__':
    unittest.main()
