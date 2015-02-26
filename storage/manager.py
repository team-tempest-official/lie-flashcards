"""
	Operations that need to be implemented:

	Deck:
		+ add_deck
		+ get_deck
		+ remove_deck
		+ add_card
		+ get_card
		+ remove_card
		+ add_attribute
		+ get_attribute
		+ remove_attribute
	Card:
		+ set_question
		+ get_question
		+ add_answer
		+ get_answer
		+ remove_answer
	Information:
		+ set_key
		+ get_key
		+ set_value
		+ get_value
		+ set_type	
		+ get_type
"""


class Manager(object):

	def __init__(self, implementation):
		self.implementation = implementation

	def add_deck(self):
		pass

	def remove_deck(self):
		pass

	def add_deck_card(self):
		pass

	def get_deck_card(self):
		pass

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
	

