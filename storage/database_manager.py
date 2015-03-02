

class DatabaseManager(object):

	def __init__(self, implementation):
		self.implementation = implementation

	def load_state(self):
		print "-- Loading state"

	def save_state(self):
		print "-- Saving state"

	def add_deck(self):
		print "-- Adding deck"
		return self.implementation.add_deck()

	def remove_deck(self, id_):
		print "-- Removing deck: " + str(id_)
		return self.implementation.remove_deck(id_)

	def add_deck_card(self, question, answers, attributes, deck_ids):
		print "-- Adding card to deck"
		return self.implementation.add_deck_card(
													question, 
													answers,
													attributes,
													deck_ids
												)

	def remove_deck_card(self, d_id_, c_id_):
		print "-- Removing card from deck: " + str(d_id_) + " " + str(c_id_)
		return self.implementation.remove_deck_card(d_id_, c_id_)

	def add_deck_attribute(self, attribute, d_id_):
		print "-- Adding deck attribute: " + str(d_id_) 
		return self.implementation.add_deck_attribute(attribute, d_id_)

	def remove_deck_attribute(self, d_id_, attribute_key):
		print "-- Removing deck attribute: " + str(d_id_)
		return self.implementation.remove_deck_attribute(d_id_, attribute_key)

	def set_card_question(self, c_id_, question):
		print "-- Set card question: "+ str(c_id_)
		return self.implementation.set_card_question(c_id_, question)

	def get_card_question(self, c_id_, d_id_=None):
		print "-- Getting card question"
		return self.implementation.get_card_question(c_id_, d_id_)

	def add_card_answer(self, c_id_, answer):
		print "-- Adding card answer: " + str(c_id_)
		return self.implementation.add_card_answer_(c_id_, answer)

	def get_card_answers(self, c_id_):
		print "-- Getting card answers: " + str(c_id_)
		return self.implementation.get_card_answers(c_id_)
		
	def remove_card_answer(self, c_id_, a_id_):
		print "-- Removing card answer: " + str(c_id_)
		return self.implementation.remove_card_answer(c_id_, a_id_)

	def add_card_attribute(self, c_id_, attribute):
		print "-- Adding card attribute: " + str(c_id_)
		return self.implementation.add_card_attribute(c_id_, attribute)

	def remove_card_attribute(self, c_id_, key):
		print "-- Removing card attribute: " + str(c_id_)
		return self.implementation.remove_card_attribute(c_id_, key)

	def add_question_attribute(self, q_id_, attribute):
		print "-- Adding question attribute"
		return self.implementation.add_question_attribute(q_id_, attribute)

	def remove_question_attribute(self, q_id_, key):
		print "-- Removing qestion attribute: " + str(q_id_)
		return self.implementation.remove_question_attribute(q_id_, key)

	def add_answer_attribute(self, a_id_, attribute):
		print "-- Adding answer attribute"
		return self.implementation.add_answer_attribute(a_id_, attribute)

	def remove_answer_attribute(self, a_id_, key):
		print "-- Removing answer attribute"
		return self.implementation.remove_answer_attribute(a_id, key)

	def create_attribute(self, key_, type_, value_):
		print "-- Creating attribute"
		return self.implementation.create_attribute(key_, type_, value_)

	def create_qa(self, attributes):
		print "-- Creating qa"
		return self.implementation.create_qa(attributes)

	def create_card(self, question, answers, attributes):
		print "-- Creating card"
		return self.implementation.create_card(question, answers, attributes)

	def create_deck(self, cards, attributes):
		print "-- Creating deck"
		return self.implementation.create_deck(cards, attributes)

