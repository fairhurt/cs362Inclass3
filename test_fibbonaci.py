
import unittest

from fibbonaci import recur_fibo

class TestFib (unittest.TestCase):
       def test1(self):
            self.assertEqual(recur_fibo(12), 144)





if __name__ == '__main__':
    unittest.main(verbosity=2)
  




