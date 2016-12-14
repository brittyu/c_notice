#!/usr/bin/env python
# encoding: utf-8

import MySQLdb
from MySQLdb.cursors import DictCursor
from DBUtils.PooledDB import PooledDB
from config import DBHOST, DBPORT, DBUSER, DBPWD, DBNAME, DBCHAR


class Database(object):
    """
    create database connect pool
    """

    _pool = None

    def __init__(self):
        self._conn = Database._get_conn()
        self._cursor = self._conn.cursor()

    @staticmethod
    def _get_conn():
        """
        use singleton pattern to return a connnetion

        @return type pool db connection
        """
        if Database._pool is None:
            _pool = PooledDB(creator=MySQLdb,
                    mincached=1,
                    maxcached=30,
                    host=DBHOST,
                    port=DBPORT,
                    user=DBUSER,
                    passwd=DBPWD,
                    db=DBNAME,
                    use_unicode=False,
                    charset=DBCHAR,
                    cursorclass=DictCursor)

        return _pool.connection()
