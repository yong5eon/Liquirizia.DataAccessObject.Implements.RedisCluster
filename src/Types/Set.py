# -*- coding: utf-8 -*-

from ..Type import Type

__all__ = (
	'Set'
)


class Set(Type):
	"""Type Helper Class for Set"""

	def len(self, key):
		return self.card(key)

	def card(self, key):
		con = self.connection
		return con.scard(key)

	def isMember(self, key, value):
		con = self.connection
		return con.ismember(key, value)

	def add(self, key, value):
		con = self.connection
		con.sadd(key, value)
		return

	def get(self, key):
		return self.members(key)

	def members(self, key):
		con = self.connection
		return con.smembers(key)

	def pop(self, key, count):
		con = self.connection
		con.spop(key, count)
		return

	def remove(self, key, value):
		con = self.connection
		con.srem(key, value)
		return

	def random(self, key, count=None):
		con = self.connection
		return con.srandmember(key, count)


