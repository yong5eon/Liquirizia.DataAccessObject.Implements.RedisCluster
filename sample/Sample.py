# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObjectHelper

from Liquirizia.DataAccessObject.Implements.RedisCluster import DataAccessObject, DataAccessObjectConfiguration

from Liquirizia.DataAccessObject.Implements.RedisCluster.Types import DataStringObject
from Liquirizia.DataAccessObject.Implements.RedisCluster.Types import DataListObject
from Liquirizia.DataAccessObject.Implements.RedisCluster.Types import DataSetObject
from Liquirizia.DataAccessObject.Implements.RedisCluster.Types import DataSortedSetObject
from Liquirizia.DataAccessObject.Implements.RedisCluster.Types import DataHashObject

import sys
import json


if __name__ == '__main__':

	# Set connection
	DataAccessObjectHelper.Set(
		'Sample',
		DataAccessObject,
		DataAccessObjectConfiguration(
			hosts=[
				'YOUR_REDIS_CLUSTER_ENDPOINT',
				...
			],  # Redis Hosts Address
		)
	)

	# Get Connection
	con = DataAccessObjectHelper.Get('Sample')

	# Get/Set Value
	con.set('sample:sample', json.dumps({
		1: 1,
		2: 2
	}))
	v = json.loads(con.get('sample:sample'))
	print(v, file=sys.stdout)
	# Set Persist
	con.persist('sample:sample')
	# Set Expires
	con.expire('sample:sample', 60)
	# Delete Value
	con.delete('sample:sample')

	# String Type
	stringType = DataStringObject(con)
	stringType.set('sample:string', 'string')
	v = stringType.get('sample:string')
	print(v, file=sys.stdout)
	v = stringType.getSet('sample:string', 'changed')
	print(v, file=sys.stdout)
	v = stringType.get('sample:string')
	print(v, file=sys.stdout)
	v = stringType.len('sample:string')
	print(v, file=sys.stdout)
	con.delete('sample:string')

	# List Type
	listType = DataListObject(con)
	for i in range(0, 5):
		listType.push('sample:list', i)
		listType.push('sample:list', i)
	v = listType.get('sample:list')
	print(v, file=sys.stdout)
	con.delete('sample:list')

	# Set Type
	setType = DataSetObject(con)
	for i in range(0, 5):
		setType.add('sample:set', i)
		setType.add('sample:set', i)
	v = setType.get('sample:set')
	print(v, file=sys.stdout)
	con.delete('sample:set')

	# SortedSet Type
	sortedSetType = DataSortedSetObject(con)
	for i in range(0, 5):
		sortedSetType.add('sample:sortedSet', i, i)
		sortedSetType.add('sample:sortedSet', i, i)
	v = sortedSetType.get('sample:sortedSet')
	print(v, file=sys.stdout)
	con.delete('sample:sortedSet')

	# Hash Type
	hashType = DataHashObject(con)
	for i in range(0, 5):
		hashType.set('sample:hash', i, i)
	v = hashType.getAll('sample:hash')
	print(v, file=sys.stdout)
	con.delete('sample:hash')
