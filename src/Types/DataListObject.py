# -*- coding: utf-8 -*-

from ..DataTypeObject import DataTypeObject

__all__ = (
	'DataListObject'
)


class DataListObject(DataTypeObject):
	"""
	Data Type Object Helper Class for List
	"""

	def index(self, key, index):
		con = self.connection
		return con.lindex(key, index)

	def len(self, key):
		con = self.connection
		return con.llen(key)

	def push(self, key, value):
		con = self.connection
		con.lpush(key, value)
		return

	def pushx(self, key, value):
		con = self.connection
		con.lpushx(key, value)
		return

	def pop(self, key):
		con = self.connection
		return con.pop(key)

	def pushReverse(self, key, value):
		con = self.connection
		con.rpush(key, value)
		return

	def pushxReverse(self, key, value):
		con = self.connection
		con.rpushx(key, value)
		return

	def popReverse(self, key):
		con = self.connection
		return con.rpop(key)

	def get(self, key, start=0, stop=-1):
		return self.range(key, start, stop)

	def range(self, key, start=0, stop=-1):
		con = self.connection
		return con.lrange(key, start, stop)

	def remove(self, key, count, value):
		con = self.connection
		con.lrem(key, count, value)
		return

	def set(self, key, index, value):
		con = self.connection
		con.lset(key, index, value)
		return

	def trim(self, key, start, stop):
		con = self.connection
		con.ltrim(key, start, stop)
		return
