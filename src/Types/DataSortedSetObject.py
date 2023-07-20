# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject

__all__ = (
	'DataSortedSetObject'
)


class DataSortedSetObject(DataTypeObject):
	"""
	Data Type Object Helper Class for Set
	"""

	def add(self, key, value, score, nx=False, xx=False, ch=False, incr=False):
		con = self.connection
		con.zadd(key, {value: score}, nx=nx, xx=xx, ch=ch, incr=incr)
		return

	def length(self, key):
		return self.card(key)

	def card(self, key):
		con = self.connection
		return con.zcard(key)

	def count(self, key, min, max):
		con = self.connection
		return con.zcount(key, min, max)

	def get(self, key, start=0, stop=-1):
		return self.range(key, start, stop)

	def range(self, key, start=0, stop=-1, score=None):
		con = self.connection
		return con.zrange(key, start, stop, score)

	def remove(self, key, value):
		con = self.connection
		con.zrem(key, value)
		return

	def score(self, key, value):
		con = self.connection
		con.zscore(con, key, value)
		return
