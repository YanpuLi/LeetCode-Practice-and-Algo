#O(n)
def isUnique(s):
     # Assuming character set is ASCII (128 characters)
        if len(s) >128:
            return False
        l = [False]*128
        for i in s:
            val = ord(i)
            if l[val]:
                return False
            l[val] = True
        return True
import unittest
class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUnique(test_string)
            self.assertFalse(actual)
if __name__ == "__main__":
    unittest.main()