from information import Information
from attribute import Attribute
from card import Card
from deck import Deck
from answer import Answer
from question import Question
from eum import Enum

class SimpleImplementation(object):

	def __init__(self):
		self._id_gen = 0
		self.decks = list()
		
	def add_deck(self):
		d = Deck(self._id_gen, list(), list())
		self.decks.append(d)
		self._id_gen += 1

	def remove_deck(self, _id):
		for i in range(len(self.decks)):
			if self.decks[i]._id == _id:
				del self.decks[i]

	def add_deck_card(self, question, answers, deck_ids):
		c = Card(self._id_gen, question, answers)
		self._id_gen += 1

		for d in self.decks:
			for i in deck_ids:
				if d._id == i:
					self._cards.append(c)


	def get_deck_card(self, _d_id, _c_id):
		for i in range(len(self.decks)):
			if self.decks[]

	def remove_deck_card(self):
		pass

	def add_deck_attribute(self):
		pass

	def remove_deck_attribute(self):
		pass

	def set_card_question(self):
		pass

	def get_card_question(self):
		pass
	
	def add_card_answer(self):
		pass

	def get_card_answer(self):
		pass

	def remove_card_answer(self):
		pass

	def set_information_key(self):
		pass

	def set_information_type(self):
		pass

	def set_information_value(self):
		pass

	def get_information_key(self):
		pass

	def get_information_type(self):
		pass

	def get_information_value(self):
		pass
	