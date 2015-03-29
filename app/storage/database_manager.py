

class Deck(object):

    def __init__(self, name):
        self.name = name


class Card(object):

	def __init__(self, deck, content, type, answers):
		self.deck = deck
		self.type = type
		self.content = content
		self.answers = answers


class Answer(object):

	def __init__(self, card, a_text):
		self.a_text
		self.card = card

