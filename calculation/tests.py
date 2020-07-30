from django.test import TestCase

class CalculationTest(TestCase):

	def test_plus(self):
		self.assertEqual(1 + 1, 2)

	def test_minus(self):
		self.assertEqual(1 - 1, 0)

	def test_multiply(self):
		self.assertEqual(1 * 2, 2)

	def test_divide(self):
		self.assertEqual(2 / 1, 2)

