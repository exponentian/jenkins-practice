from django.test import TestCase

class CalculationTest(TestCase):

	def test_sum(self):
		print('- Test sum')
		self.assertEqual(1 + 1, 2)

	def test_sum2(self):
		print('- Test sum 2')
		self.assertEqual(2 + 2, 4)

	def test_substract(self):
		print('- Test substract')
		self.assertEqual(1 - 1, 0)

	def test_multiply(self):
		print('- Test multiply')
		self.assertEqual(1 * 2, 2)

	def test_divide(self):
		print('- Test divide')
		self.assertEqual(2 / 1, 2)

