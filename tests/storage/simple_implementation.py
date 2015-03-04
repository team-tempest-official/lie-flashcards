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


	def test_create_qa(self):
		author = self.manager.create_attribute("author", "string", "AndreiRO")
		opt = self.manager.create_attribute("mode", "string", "single_option")
		q = self.manager.create_attribute("question", "string", "Say hi!")
		qa = self.manager.create_qa([author, opt, q])

		self.assertNotEqual(qa.id_, None)
		self.assertEqual(qa.attributes_, [author, opt, q])
		self.assertEqual(qa.find_attribute("author"), author)

	def test_create_card(self):
		author = self.manager.create_attribute("author", "string", "AndreiRO")
		opt = self.manager.create_attribute("mode", "string", "single_option")
		q = self.manager.create_attribute("question", "string", "Say hi!")
		a = self.manager.create_attribute("answer", "string", "hi!")

		question = self.manager.create_qa([author, opt, q])
		answer = self.manager.create_qa([author, opt, a])

		c = self.manager.create_card(question, [answer, ], [author, opt])

		l = [question, answer, c]
		for i in range(len(l) - 1):
			for j in range(i + 1, len(l)):
				self.assertNotEqual(l[i].id_, l[j].id_)

		self.assertNotEqual(c.id_, None)
		self.assertEqual(c.question_, question)
		self.assertEqual(c.answers_, [answer,])
		self.assertEqual(c.attributes_, [author, opt])

	def test_create_deck(self):
		author = self.manager.create_attribute("author", "string", "AndreiRO")
		opt = self.manager.create_attribute("mode", "string", "single_option")
		q = self.manager.create_attribute("question", "string", "Say hi!")
		a = self.manager.create_attribute("answer", "string", "hi!")

		question = self.manager.create_qa([author, opt, q])
		answer = self.manager.create_qa([author, opt, a])

		c = self.manager.create_card(question, [answer, ], [author, opt])		
		d = self.manager.create_deck([c, ], [author, ])

		l = [question, answer, c, d]
		for i in range(len(l) - 1):
			for j in range(i + 1, len(l)):
				self.assertNotEqual(l[i].id_, l[j].id_)
		
		self.assertNotEqual(d.id_, None)
		self.assertEqual(d.cards_, [c,])
		self.assertEqual(d.attributes_, [author, ])


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(SimpleImplementationTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
