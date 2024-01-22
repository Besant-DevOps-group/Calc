import unittest
from main import add,sub

class TestCalc(unittest.TestCase):
    def testadd(self):
        return self.assertEqual(add(3,2),5)
    def testsub(self):
        return self.assertEqual(sub(3,2),1)
    


if __name__=='__main__':
    unittest.main()
