def reverseList(list):
  for i in range(len(list)//2):
    list[i],list[len(list)-i-1] = list[len(list)-i-1],list[i]
  return list

def palindrome(str):
    for i in range(len(str)//2):
        if str[i] == str[len(str)-i-1]: continue
        else: return False
    return True

def coins(change):
    coin = [0,0,0,0]
    if change >= 25:
        coin[0] = change//25
        change -= coin[0]*25
    if change >= 10:
        coin[1] = change//10
        change -= coin[1]*10
    if change >= 5:
        coin[2] = change//5
        change -= coin[2]*5
    if change < 5:
        coin[3] = change
        change -= coin[3]
    return coin

import unittest

class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList([2,4,-3]), [-3,4,2])
    def test3(self):
        return self.assertEqual(reverseList([0,0,0,0,1,0,0]), [0,0,1,0,0,0,0])
    def test4(self):
        return self.assertEqual(reverseList(["a",4,"9"]), ["9",4,"a"])
class palindromeTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(palindrome("racecar"), True)
    def test2(self):
       return self.assertEqual(palindrome("rabbit"), False)
    def test3(self):
       return self.assertEqual(palindrome("tacocat"), True)
    def test4(self):
       return self.assertEqual(palindrome("920dkth6"), False)
    def test5(self):
       return self.assertEqual(palindrome("1I1I1I1"), True)
class coinsTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(coins(87), [3,1,0,2])
    def test2(self):
        return self.assertEqual(coins(93), [3,1,1,3])
    def test3(self):
        return self.assertEqual(coins(49), [1,2,0,4])
    def test4(self):
        return self.assertEqual(coins(24), [0,2,0,4])
    def test5(self):
        return self.assertEqual(coins(6), [0,0,1,1])
    def test6(self):
        return self.assertEqual(coins(199), [7,2,0,4])
if __name__ == "__main__":
    unittest.main()