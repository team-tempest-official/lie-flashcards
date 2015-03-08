

class Card(object):

	def __init__(self, _id, question, answers, attributes):
		self.id_ = _id
		self.question_ = question # single question
		self.answers_ = answers # list of answers
		self.attributes_ = attributes

	def find_attribute(self, key):
		for attr in self.attributes_:
			if attr.attribute_key_ == key:
				return attr

