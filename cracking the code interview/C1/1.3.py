import unittest
def check_permutation(s1, s2):
	if len(s1) != len(s2):
		return False
	dic1 = {}
	for i in s1:
		dic1[s1] = dic1.get(s1, 0) +1
	for j in s2:
		dic2[s2]= dic2.get(s2, 0) +1
	if dic1 == dic2:
		return True
	return False
class Test(unittest.TestCase):
	dataT = [('abcd', 'bacd'), ('3563476', '7334566'),('wef34f', 'wffe34')]
	dataF = [('abcd', 'd2cba'), ('2354', '1234'), ('dcw4f', 'dcw5f')]
	def test_cp(self):
        # true check
		for test_string in self.dataT:
			actual = check_permutation(test_string[0], test_string[1])
			self.assertTrue(actual)
        # false check
		for test_string in self.dataF:
			actual = check_permutation(test_string[0], test_string[1])
			self.assertFalse(actual)
