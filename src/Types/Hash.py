# -*- coding: utf-8 -*-

from ..Type import Type

__all__ = (
	'Hash'
)


class Hash(Type):
	"""Type Helper Class for Hash"""

	def keys(self, key):
		con = self.connection
		return con.hkeys(key)

	def get(self, key, field):
		con = self.connection
		return con.hget(key, field)

	def getAll(self, key):
		con = self.connection
		return con.hgetall(key)

	def set(self, key, field, value):
		con = self.connection
		con.hset(key, field, value)

	def remove(self, key, field):
		con = self.connection
		con.hdel(key, field)
		
	def exists(self, key, field):
		con = self.connection
		return con.hexists(key, field)
	