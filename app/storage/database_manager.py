import sqlite3

class DatabaseManager(object):

    @classmethod
    def start(cls):
        Deck.start()

    @classmethod
    def shut_down(cls):
        Deck.shut_down()

class Deck(object):
    con = sqlite3.connect('development.sql')

    def __init__(self, name=""):
        self.name=name

    @classmethod
    def create(cls, name):
        cursor = cls.con.cursor()
        try:
            cursor.execute('INSERT INTO DECKS VALUES(?)', (name,))
            cls.con.commit()
            return Deck(name=name)
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def get(cls, name):
        cursor = cls.con.cursor()
        try:
            cursor.execute('SELECT * FROM DECKS WHERE NAME = ?', (name,))
            res = cursor.fetchone()
            if res:
                return Deck(res[0])
            else:
                raise(sqlite3.Error(': object does not exist'))
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def remove(cls, name):
        if name != 'DefaultDeck':
            cursor = cls.con.cursor()
            try:
                cursor.execute('DELETE FROM DECKS WHERE NAME = ?', (name,))
                cls.con.commit()
            except sqlite3.Error, e:
                cls.con.rollback()
                print "Error %s" % e.args[0]
        else:
            print 'Cannot modify DefaultDeck.'

    @classmethod
    def clear(cls):
        cursor = cls.con.cursor()
        try:
            cursor.execute('DELETE FROM DECKS')
            cls.con.commit()
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error %s" % e.args[0]

    @classmethod
    def shut_down(cls):
        if cls.con:
            cls.con.close()

    def update(self, name):
        if name != 'DefaultDeck':
            cursor = Deck.con.cursor()
            try:
                cursor.execute('UPDATE DECKS SET NAME = ? WHERE NAME = ?', (name,self.name))
                Deck.con.commit()
            except sqlite3.Error, e:
                Deck.con.rollback()
                print "Error(update) %s" % e.args[0]
        else:
            print 'Cannot modify DefaultDeck.'



class Card(object):
    con = sqlite3.connect('development.sql')

    def __init__(self, id=1, deck=Deck.get('DefaultDeck'), content=None, _type='string:1'):
        self.id = id
        self.deck = deck
        self.type = _type
        self.content = content
        self.answers = []

    @classmethod
    def create(cls, deck_name='DefaultDeck', content=None, _type='string:1', answers=[]):
        cursor = cls.con.cursor()
        try:
            cursor.execute('INSERT INTO CARDS(TYPE, CONTENT, DECK_NAME) VALUES(?, ?, ?)', (_type, content, deck_name))
            cls.con.commit()
            card_id = cursor.lastrowid
            new_card = Card(card_id, Deck.get(deck_name), content, _type)
            for a in answers:
                new_card.answers.append(Answer.create(new_card, a))

            return new_card
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error(creation) %s" % e.args[0]


class Answer(object):
    con = sqlite3.connect('development.sql')

    def __init__(self, card, a_text):
        self.text = a_text
        self.card = card

    @classmethod
    def create(cls, card, a_text):
        cursor = cls.con.cursor()
        try:
            cursor.execute('INSERT INTO ANSWERS(CARD_ID, A_TEXT) VALUES(?, ?)', (card.id, a_text))
            cls.con.commit()
            return Answer(card, a_text)
        except sqlite3.Error, e:
            cls.con.rollback()
            print "Error(creation) %s" % e.args[0]



