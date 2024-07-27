# -*- coding: utf-8 -*-

from ..Type import Type

__all__ = (
	'String'
)


class String(Type):
	"""Type Helper Class for String"""

	def set(self, key, value):
		con = self.connection
		con.set(key, value)
		return

	def get(self, key):
		con = self.connection
		return con.get(key)

	def getSet(self, key, value):
		con = self.connection
		return con.getset(key, value)

	def len(self, key):
		con = self.connection
		return con.strlen(key)
