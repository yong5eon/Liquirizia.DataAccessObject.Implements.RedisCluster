# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Connection as BaseConnection
from Liquirizia.DataAccessObject.Properties.Cache import Cache

from rediscluster import RedisCluster

from .Configuration import Configuration

__all__ = (
	'DataAccessObject'
)


class Connection(BaseConnection, Cache):
	"""Connection Class for Redis Cluster"""
	"""
	TODO :
		* Exception Handling with Error of DataAccessObject
	"""

	def __init__(self, conf: Configuration):
		super(Connection, self).__init__(conf)
		self.conf = conf
		self.connection = None
		return

	def __del__(self):
		if self.connection:
			self.close()
		return

	def connect(self):
		self.connection = RedisCluster(
			startup_nodes=self.conf.hosts,
			decode_responses=True,
			skip_full_coverage_check=True
		)
		return

	def close(self):
		self.connection.close()
		return

	def keys(self, key):
		return self.connection.keys(key)

	def exists(self, key):
		return self.connection.exists(key)

	def set(self, key, value, expires=None):
		self.connection.set(key, value)
		if expires:
			self.connection.expire(key, expires)
		else:
			self.connection.persist(key)
		return

	def get(self, key):
		return self.connection.get(key)

	def expire(self, key, seconds):
		self.connection.expire(key, seconds)
		return

	def persist(self, key):
		self.connection.persist(key)
		return

	def delete(self, key):
		self.connection.delete(key)
		return
