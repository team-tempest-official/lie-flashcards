"""
	Operations that need to be implemented:

	Deck:
		+ add
		+ get
		+ remove
		+ add_card
		+ get_card
		+ remove_card
		+ add_attribute
		+ get_attribute
		+ remove_attribute
"""


class Manager(object):

	def __init__(self, implementation):
		self.implementation = implementation

