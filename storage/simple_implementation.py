from model.attribute import Attribute
from model.card import Card
from model.deck import Deck
from model.qa import QA


class SimpleImplementation(object):

	def __init__(self):
		self.id_gen_ = 0
		self.decks = list()
		
	def add_deck(self, d): 
		self.decks.append(d)
		self.id_gen_ += 1

	def remove_deck(self, id_):
		index = -1

		for i in range(len(self.decks)):
			if self.decks[i].id_ == id_:
				index = i

		if index != -1:
			del self.decks[index] 
			return True

		return False

	def add_deck_card(self, c, deck_ids):
		for d in self.decks:
			for i in deck_ids:
				if d.id_ == i:
					d.cards_.append(c)


	def get_deck_card(self, d_id_, c_id_):
		for d in self.decks:
			if d.id_ == d_id_:
				for c in d.cards_:
					if c.id_ == c_id_:
						return c

	def remove_deck_card(self, d_id_, c_id_):
		index = -1

		for d in self.decks:
			if d.id_ == d_id_:
				for j in range(len(d.cards_)):
					if d.cards_[j].id_ == c_id_:
						index = j
				if index != -1:
					del d.cards_[index]
					return True

		return False

	def add_deck_attribute(self, d_id_, attribute):
		for d in self.decks:
			if d.id_ == d_id_:
				d.attributes_.append(attribute)

	def remove_deck_attribute(self, d_id_, attribute_key):
		index = -1

		for d in self.decks:
			if d.id_ == d_id_:
				for i in range(len(d.attributes_)):
					if d.attributes_[i].attribute_key_ == attribute_key:
						index = i
				if index != -1:
					del d.attributes_[index]
					return True

		return False

	def set_card_question(self, c_id_, question):
		for d in self.decks:
			for j in range(len(d.cards_)):
				if d.cards_[j].id_ == c_id_:
					d.cards_[j].question_ = question


	def get_card_question(self, c_id_, d_id_=None):
		if d_id_ == None:
			for d in self.decks:
				for c in d.cards_:
					if c.id_ == c_id_:
						return c.question
		else:
			for d in self.decks:
				if d.id_ == d_id_:
					for c in d.cards_:
						if c.id_ == c_id_:
							return c.question
	
	def add_card_answer(self, c_id_, answer):
		for d in self.decks:
			for c in d.cards_:
				if c.id_ == c_id_:
					c.answers_.append(answer)


	def get_card_answers(self, c_id_):
		for d in self.decks:
			for c in d.cards_:
				if c.id_ == c_id_:
					return c.answers_	

	def remove_card_answer(self, c_id_, a_id_):
		index = -1

		for d in self.decks:
			for c in d.cards_:
				if c.id_ == c_id_:
					for i in len(c.answers_):
						if c.answers_[i].id_ == a_id_:
							index = i
					if index != -1:
						del c.answers_[index]
						index = -1

	def add_card_attribute(self, c_id_, attribute):
		for d in self.decks:
			for c in d.cards_:
				if c.id_ == c_id_:
					c.attributes_.append(attribute)
	
	def remove_card_attribute(self, c_id_, key):
		index = -1

		for d in self.decks:
			for c in d.cards_:
				if c.id_ == c_id_:
					for i in range(len(c.attributes_)):
						if c.attributes_[i].key == key:
							index = i
					if index != -1:
						del c.attributes_[index]
						index = -1

	def add_question_attribute(self, q_id_, attribute):
		for d in self.decks:
			for c in d.cards_:
				if c.question_.id_ == q_id_:
					c.question_.attributes_.append(attribute)

	def remove_question_attribute(self, q_id_, key):
		index = -1

		for d in self.decks:
			for c in d.cards_:
				if c.question_.id_ == q_id_:
					for i in range(len(c.question_.attributes_)):
						if c.question_.attributes_[i].key == key:
							index = i
					if index != -1:
						del c.question_.attributes_[i]
						index = -1

	def add_answer_attribute(self, a_id_, attribute):
		for d in self.decks:
			for c in d.cards_:
				for a in c.answers_:
					if a.id_ == a_id_:
						c.question_.attributes_.append(attribute)

	def remove_answer_attribute(self, a_id_, key):
		index = -1

		for d in self.decks:
			for c in d.cards_:
				for a in c.answers:
					if a.id_ == a_id_:
					
						for i in range(len(a.attributes_)):
							if a.attributes_[i].key == key:
								index = i
						if index != -1:
							del a.attributes_[i]
							index = -1


	def create_attribute(self, key_, type_, value_):
		return Attribute(key_, value_, type_)
		
	def create_qa(self, attributes):
		qa = QA(self.id_gen_, attributes)
		self.id_gen_ += 1

		return qa

	def create_card(self, question, answers, attributes):
		c = Card(self.id_gen_, question, answers, attributes)
		self.id_gen_ += 1

		return c

	def create_deck(self, cards, attributes):
		d = Deck(self.id_gen_, cards, attributes)
		self.id_gen_ += 1

		return d
	
