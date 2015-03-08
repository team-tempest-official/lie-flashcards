

class Deck(object):

	def __init__(self, id_, cards, attributes):
		self.cards_ = cards
		self.attributes_ = attributes
		self.id_ = id_

	def find_attribute(self, key):
		for attr in self.attributes_:
			if attr.attribute_key_ == key:
				return attr
