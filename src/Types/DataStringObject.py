# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject

__all__ = (
	'DataStringObject'
)


class DataStringObject(DataTypeObject):
	"""
	Data Type Object Helper Class for String
	"""

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
