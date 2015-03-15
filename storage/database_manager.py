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

	def generate_data(self, decks = 1):
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
								  "What is the name of the app?"),
			self.create_attribute("question", "string", "mincinos"),
			self.create_attribute("question", "string", "dominatie"),
			self.create_attribute("question", "string", "febra"),
			self.create_attribute("question", "string", "liniste"),
			self.create_attribute("question", "string", "nimeni"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "apel"),
			self.create_attribute("question", "string", "ciudat"),
			self.create_attribute("question", "string", "bani"),
			self.create_attribute("question", "string", "circ"),
			self.create_attribute("question", "string", "otrava"),
			self.create_attribute("question", "string", "parte"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "mult"),
			self.create_attribute("question", "string", "tot"),
			self.create_attribute("question", "string", "mereu"),
			self.create_attribute("question", "string", "cateodata"),
			self.create_attribute("question", "string", "uneori"),
			self.create_attribute("question", "string", "cale"),
			self.create_attribute("question", "string", "tipat/urlet/strigat"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "amintiri"),
			self.create_attribute("question", "string", "totul"),
			self.create_attribute("question", "string", "vant"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "cutin"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "piele"),
			self.create_attribute("question", "string", "maine"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "cum"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "adevarat"),
			self.create_attribute("question", "string", "puls"),
			self.create_attribute("question", "string", "hipnotizare"),
			self.create_attribute("question", "string", "inteles"),
			self.create_attribute("question", "string", "razboinic"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "revolutie"),
			self.create_attribute("question", "string", "cimitir"),
			self.create_attribute("question", "string", "ostil"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "furtuna"),
			self.create_attribute("question", "string", "furie"),
			self.create_attribute("question", "string", "rapid"),
			self.create_attribute("question", "string", "totul"),
			self.create_attribute("question", "string", "sau"),
			self.create_attribute("question", "string", "nimic"),
			self.create_attribute("question", "string", "stupefiat"),
			self.create_attribute("question", "string", "jurnal"),
			self.create_attribute("question", "string", "voce"),
			self.create_attribute("question", "string", "dark")
		]

		qs1 = [
			self.create_attribute("question", "string", "glinda"),
			self.create_attribute("question", "string", "bratara"),
			self.create_attribute("question", "string", "isteric"),
			self.create_attribute("question", "string", "sange"),
			self.create_attribute("question", "string", "mort"),
			self.create_attribute("question", "string", "criminal"),
			self.create_attribute("question", "string", "cheie"),
			self.create_attribute("question", "string", "agenda"),
			self.create_attribute("question", "string", "tastatura"),
			self.create_attribute("question", "string", "setari"),
			self.create_attribute("question", "string", "putere"),
			self.create_attribute("question", "string", "voce"),
			self.create_attribute("question", "string", "cronometru"),
			self.create_attribute("question", "string", "greautate"),
			self.create_attribute("question", "string", "arie"),
			self.create_attribute("question", "string", "sunet"),
			self.create_attribute("question", "string", "iaurt"),
			self.create_attribute("question", "string", "destul"),
			self.create_attribute("question", "string", "inca"),
			self.create_attribute("question", "string", "daca"),
			self.create_attribute("question", "string", "numai"),
			self.create_attribute("question", "string", "doar"),
			self.create_attribute("question", "string", "suferinta"),
			self.create_attribute("question", "string", "depresie"),
			self.create_attribute("question", "string", "farfurie"),
			self.create_attribute("question", "string", "transpirat"),
			self.create_attribute("question", "string", "frig"),
			self.create_attribute("question", "string", "pana"),
			self.create_attribute("question", "string", "aici"),
			self.create_attribute("question", "string", "sigur"),
			self.create_attribute("question", "string", "ploaie"),
			self.create_attribute("question", "string", "zapada"),
			self.create_attribute("question", "string", "distrus"),
			self.create_attribute("question", "string", "peste"),
			self.create_attribute("question", "string", "altul/alta"),
			self.create_attribute("question", "string", "loc"),
			self.create_attribute("question", "string", "punct"),
			self.create_attribute("question", "string", "autoritate"),
			self.create_attribute("question", "string", "lebada"),
			self.create_attribute("question", "string", "in"),
			self.create_attribute("question", "string", "fara"),
			self.create_attribute("question", "string", "tarziu"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "fara"),
			self.create_attribute("question", "string", "razboi"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "greu"),
			self.create_attribute("question", "string", "creier"),
			self.create_attribute("question", "string", "frica"),
			self.create_attribute("question", "string", "sacrificiu"),
			self.create_attribute("question", "string", "bantuit"),
			self.create_attribute("question", "string", "nor"),
			self.create_attribute("question", "string", "a"),
			self.create_attribute("question", "string", "atat")
		]

		ans = [
			self.create_attribute("answer", "string", "..."),
			self.create_attribute("answer", "string", "10"),
			self.create_attribute("answer", "string", "Bucharest"),
			self.create_attribute("answer", "string", "Lie"),
			self.create_attribute("answer", "string", " liar"),
			self.create_attribute("answer", "string", " domination"),
			self.create_attribute("answer", "string", " fever"),
			self.create_attribute("answer", "string", " silence"),
			self.create_attribute("answer", "string", " nobody"),
			self.create_attribute("answer", "string", " to listen"),
			self.create_attribute("answer", "string", " call"),
			self.create_attribute("answer", "string", " freaky"),
			self.create_attribute("answer", "string", " money"),
			self.create_attribute("answer", "string", " circus"),
			self.create_attribute("answer", "string", " poison"),
			self.create_attribute("answer", "string", " piece"),
			self.create_attribute("answer", "string", " to give"),
			self.create_attribute("answer", "string", " more"),
			self.create_attribute("answer", "string", " everytime"),
			self.create_attribute("answer", "string", " always"),
			self.create_attribute("answer", "string", " sometimes"),
			self.create_attribute("answer", "string", " often"),
			self.create_attribute("answer", "string", " way"),
			self.create_attribute("answer", "string", " scream"),
			self.create_attribute("answer", "string", " to count"),
			self.create_attribute("answer", "string", " memories"),
			self.create_attribute("answer", "string", " everything"),
			self.create_attribute("answer", "string", " wind"),
			self.create_attribute("answer", "string", " to change"),
			self.create_attribute("answer", "string", " knive"),
			self.create_attribute("answer", "string", " to shut up"),
			self.create_attribute("answer", "string ", "to drive"),
			self.create_attribute("answer", "string", " to stop"),
			self.create_attribute("answer", "string", " skin"),
			self.create_attribute("answer", "string", " tomorrow"),
			self.create_attribute("answer", "string", " to teach"),
			self.create_attribute("answer", "string", " how"),
			self.create_attribute("answer", "string", " to meet"),
			self.create_attribute("answer", "string", " true"),
			self.create_attribute("answer", "string", " pulse"),
			self.create_attribute("answer", "string", " hypnotize"),
			self.create_attribute("answer", "string", " meaning"),
			self.create_attribute("answer", "string", " warrior"),
			self.create_attribute("answer", "string", " to walk"),
			self.create_attribute("answer", "string", " revolution"),
			self.create_attribute("answer", "string", " cemetery"),
			self.create_attribute("answer", "string", " hostile"),
			self.create_attribute("answer", "string", " to let"),
			self.create_attribute("answer", "string", " storm"),
			self.create_attribute("answer", "string", " fury"),
			self.create_attribute("answer", "string", " fast"),
			self.create_attribute("answer", "string", " all"),
			self.create_attribute("answer", "string", " or"),
			self.create_attribute("answer", "string", " nothing"),
			self.create_attribute("answer", "string", " stupify"),
			self.create_attribute("answer", "string", " diary"),
			self.create_attribute("answer", "string", " whisper"),
			self.create_attribute("answer", "string", " intuneric")

		]

		ans1 = [
			self.create_attribute("answer", "string", " mirror"),
			self.create_attribute("answer", "string", " bracellet"),
			self.create_attribute("answer", "string", " insane"),
			self.create_attribute("answer", "string", " blood"),
			self.create_attribute("answer", "string", " dead"),
			self.create_attribute("answer", "string", " killer"),
			self.create_attribute("answer", "string", " key"),
			self.create_attribute("answer", "string", " phonebook"),
			self.create_attribute("answer", "string", " keypad"),
			self.create_attribute("answer", "string", " settings"),
			self.create_attribute("answer", "string", " power"),
			self.create_attribute("answer", "string", " voice"),
			self.create_attribute("answer", "string", " stopwatch"),
			self.create_attribute("answer", "string", " weight"),
			self.create_attribute("answer", "string", " area"),
			self.create_attribute("answer", "string", " sound"),
			self.create_attribute("answer", "string", " yogurt"),
			self.create_attribute("answer", "string", " enough"),
			self.create_attribute("answer", "string", " yet"),
			self.create_attribute("answer", "string", " if"),
			self.create_attribute("answer", "string", " only"),
			self.create_attribute("answer", "string", " just"),
			self.create_attribute("answer", "string", " pain"),
			self.create_attribute("answer", "string", " sadness"),
			self.create_attribute("answer", "string", " plate"),
			self.create_attribute("answer", "string", " sweat"),
			self.create_attribute("answer", "string", " cold"),
			self.create_attribute("answer", "string", " until"),
			self.create_attribute("answer", "string", " here"),
			self.create_attribute("answer", "string", " safe"),
			self.create_attribute("answer", "string", " rain"),
			self.create_attribute("answer", "string", " snow"),
			self.create_attribute("answer", "string", " broken"),
			self.create_attribute("answer", "string", " over"),
			self.create_attribute("answer", "string", " other"),
			self.create_attribute("answer", "string", " place"),
			self.create_attribute("answer", "string", " point"),
			self.create_attribute("answer", "string", " autority"),
			self.create_attribute("answer", "string", " swan"),
			self.create_attribute("answer", "string", " alive"),
			self.create_attribute("answer", "string", " untitled"),
			self.create_attribute("answer", "string", " late"),
			self.create_attribute("answer", "string", " to believe"),
			self.create_attribute("answer", "string", " to hit"),
			self.create_attribute("answer", "string", " to keep"),
			self.create_attribute("answer", "string", " without"),
			self.create_attribute("answer", "string", " war"),
			self.create_attribute("answer", "string", " to follow"),
			self.create_attribute("answer", "string", " hard"),
			self.create_attribute("answer", "string", " brain"),
			self.create_attribute("answer", "string", " fear"),
			self.create_attribute("answer", "string", " sacrifice"),
			self.create_attribute("answer", "string", " haunted"),
			self.create_attribute("answer", "string", " cloud"),
			self.create_attribute("answer", "string", " to waste"),
			self.create_attribute("answer", "string", " so close")

		]

		name = self.create_attribute("name", "string", "Generated Deck")
		name1 = self.create_attribute("name", "string", "Fun Deck")

		i = 0
		while i < decks:
			cards = []
			cards1 = []
			j = 0
			while j < len(qs):
				q = self.create_qa([qs[j], author, date, opt])
				a = self.create_qa([ans[j], author, date, opt])
				cards.append(self.create_card(q, [a,], [author, date]))
				j += 1

			j = 0
			while j < len(qs1):
				q = self.create_qa([qs1[j], author, date, opt])
				a = self.create_qa([ans1[j], author, date, opt])
				cards1.append(self.create_card(q, [a,], [author, date]))
				j += 1

			d = self.create_deck(cards, [author, date, name])
			e = self.create_deck(cards1, [author, date, name1])

			self.add_deck(e)
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

	def find_card_by_qa(self, qa):
		cards = []
		for d in self.implementation.decks:
			for c in d.cards_:
				if qa is c.question_:
					return c


	def find_deck_by_attribute(self, attribute_key, attribute_value):
		decks = []
		for d in self.implementation.decks:
			for a in d.attributes_:
				if a.attribute_key_ == attribute_key and \
					a.attribute_value_ == attribute_value and \
					d not in decks:
					decks.append(d)

		return decks
