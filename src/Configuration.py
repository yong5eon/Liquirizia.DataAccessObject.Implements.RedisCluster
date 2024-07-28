# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Configuration as BaseConfiguration

__all__ = (
	'Configuration'
)


class Configuration(BaseConfiguration):
	"""Configuration Class for Redis"""

	def __init__(self, hosts: list, username=None, password=None):
		self.hosts = []
		for host in hosts:
			if isinstance(host, str):
				self.hosts.append({
					'host': host,
					'port': 6379
				})
				continue
			if isinstance(host, (list, tuple)) and isinstance(host[0], str) and isinstance(host[1], int):
				self.hosts.append({
					'host': host[0],
					'port': host[1]
				})
		if len(self.hosts) == 0:
			raise RuntimeError('hosts is invalid')
		self.user = username
		self.password = password
		return
