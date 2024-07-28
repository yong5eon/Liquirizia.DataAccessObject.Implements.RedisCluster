# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Type as BaseType

from .Connection import Connection

__all__ = (
	'Type'
)


class Type(BaseType):
	"""Abstract Type Class for Redis"""

	def __init__(self, con: Connection):
		self.connection = con.connection
		return
