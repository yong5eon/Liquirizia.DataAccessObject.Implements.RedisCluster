# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataTypeObject as DataTypeObjectBase

from .DataAccessObject import DataAccessObject

__all__ = (
	'DataTypeObject'
)


class DataTypeObject(DataTypeObjectBase):
	"""
	Data Type Object Abstract Class for Redis
	"""

	def __init__(self, obj: DataAccessObject):
		self.connection = obj.connection
		return
