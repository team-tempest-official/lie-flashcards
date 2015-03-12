import time

class DatabaseManager(object):

	def __init__(self, implementation, log = False):
		self.implementation = implementation
		self.to_log = log

	def load_state(self):
		if self.to_log:
			print "-- Loading state"

	def save_state(self):
		if self.to_log:
			print "-- Saving state"

	def add_deck(self, d):
		if self.to_log:
			print "-- Adding deck"
		return self.implementation.add_deck(d)

	def remove_deck(self, id_):
		if self.to_log:
			print "-- Removing deck: " + str(id_)
		return self.implementation.remove_deck(id_)

	def add_deck_card(self, c, deck_ids):
		if self.to_log:
			print "-- Adding card to deck"
		return self.implementation.add_deck_card(c,	deck_ids)
	def remove_deck_card(self, d_id_, c_id_):
		if self.to_log:
			print "-- Removing card from deck: " + str(d_id_) + " " + str(c_id_)
		return self.implementation.remove_deck_card(d_id_, c_id_)

	def add_deck_attribute(self, d_id_, attribute):
		if self.to_log:
			print "-- Adding deck attribute: " + str(d_id_)
		return self.implementation.add_deck_attribute(d_id_, attribute)

	def remove_deck_attribute(self, d_id_, attribute_key):
		if self.to_log:
			print "-- Removing deck attribute: " + str(d_id_)
		return self.implementation.remove_deck_attribute(d_id_, attribute_key)

	def set_card_question(self, c_id_, question):
		if self.to_log:
			print "-- Set card question: "+ str(c_id_)
		return self.implementation.set_card_question(c_id_, question)

	def get_card_question(self, c_id_, d_id_=None):
		if self.to_log:
			print "-- Getting card question"
		return self.implementation.get_card_question(c_id_, d_id_)

	def add_card_answer(self, c_id_, answer):
		if self.to_log:
			print "-- Adding card answer: " + str(c_id_)
		return self.implementation.add_card_answer(c_id_, answer)

	def get_card_answers(self, c_id_):
		if self.to_log:
			print "-- Getting card answers: " + str(c_id_)
		return self.implementation.get_card_answers(c_id_)

	def remove_card_answer(self, c_id_, a_id_):
		if self.to_log:
			print "-- Removing card answer: " + str(c_id_)
		return self.implementation.remove_card_answer(c_id_, a_id_)

	def add_card_attribute(self, c_id_, attribute):
		if self.to_log:
			print "-- Adding card attribute: " + str(c_id_)
		return self.implementation.add_card_attribute(c_id_, attribute)

	def remove_card_attribute(self, c_id_, key):
		if self.to_log:
			print "-- Removing card attribute: " + str(c_id_)
		return self.implementation.remove_card_attribute(c_id_, key)

	def add_question_attribute(self, q_id_, attribute):
		if self.to_log:
			print "-- Adding question attribute"
		return self.implementation.add_question_attribute(q_id_, attribute)

	def remove_question_attribute(self, q_id_, key):
		if self.to_log:
			print "-- Removing qestion attribute: " + str(q_id_)
		return self.implementation.remove_question_attribute(q_id_, key)

	def add_answer_attribute(self, a_id_, attribute):
		if self.to_log:
			print "-- Adding answer attribute"
		return self.implementation.add_answer_attribute(a_id_, attribute)

	def remove_answer_attribute(self, a_id_, key):
		if self.to_log:
			print "-- Removing answer attribute"
		return self.implementation.remove_answer_attribute(a_id_, key)

	def create_attribute(self, key_, type_, value_):
		if self.to_log:
			print "-- Creating attribute"
		return self.implementation.create_attribute(key_, type_, value_)

	def create_qa(self, attributes):
		if self.to_log:
			print "-- Creating qa"
		return self.implementation.create_qa(attributes)

	def create_card(self, question, answers, attributes):
		if self.to_log:
			print "-- Creating card"
		return self.implementation.create_card(question, answers, attributes)

	def create_deck(self, cards, attributes):
		if self.to_log:
			print "-- Creating deck"
		return self.implementation.create_deck(cards, attributes)

	def generate_data(self, decks=2):
		author = self.create_attribute("author", "string", "AndreiRO")
		date = self.create_attribute("date", "string", time.strftime("%d:%m:%Y"))
		opt  = self.create_attribute("type", "string", "single answer")

		qs = [
			self.create_attribute("question", "string", "What's your name?"),
			self.create_attribute("question", "string", "9+1=?"),
			self.create_attribute("question",
								  "string",
								  "What is the capital of Romania?"),
			self.create_attribute("question",
								  "string",
								  "What is the name of the app?")
		]
		ans = [
			self.create_attribute("answer", "string", "..."),
			self.create_attribute("answer", "string", "10"),
			self.create_attribute("answer", "string", "Bucharest"),
			self.create_attribute("answer", "string", "Lie")
		]

		name = self.create_attribute("name", "string", "Generated Deck")

		i = 0
		while i < decks:
			cards = []
			j = 0
			while j < len(qs):
				q = self.create_qa([qs[j], author, date, opt])
				a = self.create_qa([ans[j], author, date, opt])
				cards.append(self.create_card(q, [a,], [author, date]))
				j += 1

			d = self.create_deck(cards, [author, date, name])
			self.add_deck(d)
			i += 1

	def find_card_by_attribute(self, attribute_key, attribute_value):
		cards = []
		for d in self.implementation.decks:
			for c in d.cards_:
				for a in c.attributes_:
					if a.attribute_key_ == attribute_key and \
					   a.attribute_value_ == attribute_value and \
						c not in cards:
						cards.append(c)
		return cards


	def find_question_by_attribute(self, attribute_key, attribute_value):
		qs = []
		for d in self.implementation.decks:
			for c in d.cards_:
				for a in c.question_.attributes_:
					if a.attribute_key_ == attribute_key and \
					   a.attribute_value_ == attribute_value and \
						c.question_ not in qs:
						qs.append(c.question_)
		return qs



	def find_answer_by_attribute(self, attribute_key, attribute_value):
		ans = []
		for d in self.implementation.decks:
			for c in d.cards_:
				for an in c.answers_:
					for a in an.attributes_:
						if a.attribute_key_ == attribute_key and \
					   		a.attribute_value_ == attribute_value and \
							an not in ans:
							ans.append(an)

		return ans

	def find_deck_by_attribute(self, attribute_key, attribute_value):
		decks = []
		for d in self.implementation.decks:
			for a in d.attributes_:
				if a.attribute_key_ == attribute_key and \
					a.attribute_value_ == attribute_value and \
					d not in decks:
					decks.append(d)

		return decks
