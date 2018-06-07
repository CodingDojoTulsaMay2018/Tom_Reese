# not finished


class MathDojo:
    def __init__(self,name):
        self.name = name
        self.total = 0
    def add(self,*args):
        pass
        sum = 0
        for i in args:
            sum+=i
        print(sum)
        self.total += sum
        return self
    def subtract(self,*args):
        pass
        sum = 0
        for i in args:
            sum-=i
        print(sum)
        self.total += sum
        return self
    def result(self):
        pass
        result = self.total
        print(result)
        self.total= 0

import unittest 

class addTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(add([1,3,5]), [5,3,1])
class subtractTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(subtract("racecar"), True)
class resultTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(result(87), [3,1,0,2])
    def setUp(self): 
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")
if __name__ == "__main__":
    unittest.main()