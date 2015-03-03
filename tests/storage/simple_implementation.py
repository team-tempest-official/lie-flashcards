from storage.database_manager import DatabaseManager
from storage.simple_implementation import SimpleImplementation
import unittest

class SimpleImplementationTest(unittest.TestCase):

	def setUp(self):
		self.manager = DatabaseManager(SimpleImplementation())

	def tearDown(self):
		pass

	def test_create_attribute(self):
		author = self.manager.create_attribute("author", "string", "AndreiRO")		
		self.assertEqual(author.attribute_key_, "author")
		self.assertEqual(author.attribute_type_, "string")
		self.assertEqual(author.attribute_value_, "AndreiRO")

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(SimpleImplementationTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
