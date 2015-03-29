

class Deck(object):

    def __init__(self, name):
        self.name = name


class Card(object):

	def __init__(self, deck, question, type, answers):
		self.deck = deck
		self.type = type
		self.question = question
		self.answers = answers


class Answers(object):

	def __init__(self, card, text):
		self.text = text
		self.card = card

