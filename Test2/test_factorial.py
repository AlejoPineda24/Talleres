import unittest
from Funciones2.factorial import factorial

class TestFactorial(unittest.TestCase):
	
	def test_factorial_5(self):
		self.assertEqual(factorial(5), 120)
	
	def test_factorial_3(self):
		self.assertEqual(factorial(3), 6)

if __name__ == '__main__':
	unittest.main()
print(test_factorial_5)
print(test_factorial_3)