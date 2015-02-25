

class Deck(object):

	def __init__(self, cards, attributes):
		self.cards = cards
		self.attributes = attributes

	def get_attribute(attribute_key):
		for attr in attributes:
			if attr.attribute_key == attribute_key:
				return attr

	def add_attribute(attribute):
		self.attributes.append(attribute)
	
	def get_card(card):
		for c in cards:
			if c == card:
				return c

	def add_card(card):
		self.cards.append(card)
