#!/usr/bin/env python
from storage.database_manager import DatabaseManager
from storage.simple_implementation import SimpleImplementation
import unittest
from random import randint


class SimpleImplementationTest(unittest.TestCase):

	MAGIC_NUMBER = 100

	def setUp(self):
		self.manager = DatabaseManager(SimpleImplementation())

	def tearDown(self):
		self.manager.implementation.id_gen_ = 0

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

	def test_add_deck(self):
		author = self.manager.create_attribute("author", "string", "AndreiRO")
		opt = self.manager.create_attribute("mode", "string", "single_option")
		q = self.manager.create_attribute("question", "string", "Say hi!")
		a = self.manager.create_attribute("answer", "string", "hi!")

		question = self.manager.create_qa([author, opt, q])
		answer = self.manager.create_qa([author, opt, a])

		c = self.manager.create_card(question, [answer, ], [author, opt])		
		d = self.manager.create_deck([c, ], [author, ])

		self.manager.add_deck(d)
		self.assertEqual(self.manager.implementation.decks, [d, ])

		i = 0
		while i < SimpleImplementationTest.MAGIC_NUMBER:
			i += 1
			self.manager.add_deck(self.manager.create_deck(list(), list()))

		self.assertEqual(i + 1, len(self.manager.implementation.decks))

	def test_remove_deck(self):
		author = self.manager.create_attribute("author", "string", "AndreiRO")
		opt = self.manager.create_attribute("mode", "string", "single_option")
		q = self.manager.create_attribute("question", "string", "Say hi!")
		a = self.manager.create_attribute("answer", "string", "hi!")

		question = self.manager.create_qa([author, opt, q])
		answer = self.manager.create_qa([author, opt, a])

		c = self.manager.create_card(question, [answer, ], [author, opt])		
		d = self.manager.create_deck([c, ], [author, ])
		self.manager.add_deck(d)

		self.assertTrue(self.manager.remove_deck(d.id_))
		self.assertEqual(self.manager.implementation.decks, list())

		i = 0
		while i < SimpleImplementationTest.MAGIC_NUMBER:
			i += 1
			self.manager.add_deck(self.manager.create_deck(list(), list()))

		self.assertEqual(i, len(self.manager.implementation.decks))

		i = 0
		while i < SimpleImplementationTest.MAGIC_NUMBER:
			self.manager.remove_deck(self.manager.remove_deck(self.manager.implementation.decks[0].id_))
			i += 1

		self.assertEqual(0, len(self.manager.implementation.decks))

	def test_add_deck_card(self):
		i = 0
		while i < SimpleImplementationTest.MAGIC_NUMBER:
			d = self.manager.create_deck(list(), list())
			self.manager.add_deck(d)
			i += 1

		ids = []
		i = 0

		while i < SimpleImplementationTest.MAGIC_NUMBER:
			to_add = randint(1,10)
			if to_add % 2 == 0:
				ids.append(self.manager.implementation.decks[i].id_)
			i += 1

		c = self.manager.create_card(None, list(), list())
		self.manager.add_deck_card(c, ids)
		added = 0
		for d in self.manager.implementation.decks:
			if d.id_ in ids:
				added += 1
				self.assertTrue(c in d.cards_)

		self.assertEqual(added, len(ids))

	def test_remove_deck_card(self):
		i = 0
		while i < SimpleImplementationTest.MAGIC_NUMBER:
			d = self.manager.create_deck(list(), list())
			self.manager.add_deck(d)
			i += 1

		ids = []
		i = 0

		while i < SimpleImplementationTest.MAGIC_NUMBER:
			to_add = randint(1,10)
			if to_add % 2 == 0:
				ids.append(self.manager.implementation.decks[i].id_)
			i += 1

		c = self.manager.create_card(None, list(), list())
		self.manager.add_deck_card(c, ids)
		deleted = 0
		for d in self.manager.implementation.decks:
			if d.id_ in ids:
				self.manager.remove_deck_card(d.id_, c.id_)
				self.assertTrue(c not in d.cards_)
				deleted += 1

		self.assertEqual(deleted, len(ids))

	def test_add_deck_attribute(self):
		attributes = []
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "string")
		a3 = self.manager.create_attribute("a3", "v3", "string")

		d = self.manager.create_deck(list(),[a1, a2])
		self.manager.add_deck(d)
		self.assertTrue(a1 in self.manager.implementation.decks[0].attributes_)
		self.assertTrue(a2 in self.manager.implementation.decks[0].attributes_)

		self.manager.add_deck_attribute(d.id_, a3)
		self.assertTrue(a3 in self.manager.implementation.decks[0].attributes_)


	def test_remove_deck_attribute(self):
		attributes = []
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "string")
		a3 = self.manager.create_attribute("a3", "v3", "string")

		d = self.manager.create_deck(list(),[a1, a2, a3])
		self.manager.add_deck(d)
		
		self.manager.remove_deck_attribute(d.id_, "a2")
		self.assertTrue(a2 not in self.manager.implementation.decks[0].attributes_)
		self.assertTrue(a1 in self.manager.implementation.decks[0].attributes_)
		self.assertTrue(a3 in self.manager.implementation.decks[0].attributes_)

	def test_set_card_question(self):
		c = self.manager.create_card(None, list(), list())
		q = self.manager.create_qa(list())
		d = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d)

		self.assertEqual(c.question_, None)
		self.manager.set_card_question(c.id_, q)
		self.assertEqual(c.question_, q)

	def test_get_card_question(self):
		c = self.manager.create_card(None, list(), list())
		q = self.manager.create_qa(list())
		d = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d)
		self.manager.set_card_question(c.id_, q)
		self.assertEqual(q, self.manager.get_card_question(c.id_, d.id_))
	
	def test_add_card_answer(self):
		c = self.manager.create_card(None, list(), list())
		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())
		a = self.manager.create_qa(list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)

		self.manager.add_card_answer(c.id_, a)
		self.assertEqual(c.answers_[0], a)
		self.assertEqual(len(c.answers_), 1)

	def test_get_card_answers(self):
		a1 = self.manager.create_qa(list())
		a2 = self.manager.create_qa(list())
		c = self.manager.create_card(None, [a1, a2], list())
		d = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d)
		self.assertEqual([a1, a2], self.manager.get_card_answers(c.id_))

	def test_remove_card_answer(self):
		a1 = self.manager.create_qa(list())
		a2 = self.manager.create_qa(list())
		c = self.manager.create_card(None, [a1, a2], list())
		d = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d)
		self.manager.remove_card_answer(c.id_, a2.id_)
		self.assertEqual([a1, ], self.manager.get_card_answers(c.id_))		
	
	def test_add_card_attribute(self):
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "strng")
		c = self.manager.create_card(None, list(), list())
		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)

		self.manager.add_card_attribute(c.id_, a1)
		self.manager.add_card_attribute(c.id_, a2)

		self.assertEqual(c.attributes_, [a1, a2])
		
	def test_remove_card_attribute(self):
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "strng")
		c = self.manager.create_card(None, list(), [a1, a2])
		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)

		self.manager.remove_card_attribute(c.id_, "a2")
		self.assertEqual(c.attributes_, [a1,])

		
	def test_add_question_attribute(self):
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "strng")
		q = self.manager.create_qa(list())
		c = self.manager.create_card(q, list(), list())

		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)

		self.manager.add_question_attribute(q.id_, a1)
		self.manager.add_question_attribute(q.id_, a2)

		self.assertEqual(q.attributes_, [a1, a2])
	
	def remove_question_attribute(self):
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "strng")
		q = self.manager.create_qa([a1, a2])
		c = self.manager.create_card(q, list(), list())

		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)

		self.manager.remove_question_attribute(q.id_, "a2")
		self.assertEqual(q.attributes_, [a1])
	
	def test_add_answer_attribute(self):
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "strng")
		ans = self.manager.create_qa(list())
		c = self.manager.create_card(None, [ans, ], list())

		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)

		self.manager.add_answer_attribute(ans.id_, a1)
		self.manager.add_answer_attribute(ans.id_, a2)

		self.assertEqual(ans.attributes_, [a1, a2])

	def test_remove_answer_attribute(self):
		a1 = self.manager.create_attribute("a1", "v1", "string")
		a2 = self.manager.create_attribute("a2", "v2", "strng")
		ans = self.manager.create_qa([a1, a2])
		c = self.manager.create_card(None, [ans, ], list())

		d1 = self.manager.create_deck([c, ], list())
		d2 = self.manager.create_deck([c, ], list())

		self.manager.add_deck(d1)
		self.manager.add_deck(d2)
		self.manager.remove_answer_attribute(ans.id_, "a2")

		self.assertEqual(ans.attributes_, [a1])


if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(SimpleImplementationTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
	
