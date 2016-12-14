#!/usr/bin/env python
# encoding: utf-8

import re
import time
import json
from database import Database


class Parse(object):

    _total_page = None
    _mysql_connect = None

    def __init__(self):
        self._mysql_connect = Database()

    def _get_json_str(self, response_text):
        p = re.compile(r'(.*)')
        result = p.findall(response_text)

        return result[0][2:][:-2]

    def get_total_page(self):
        return self._total_page

    def str_2_time(self, time_str):
        p = re.compile(r'\d{2,}')
        time_list = p.findall(time_str)
        time_str = time_list[0] + '-' \
                + time_list[1] + '-' \
                + time_list[2]
        time_array = time.strptime(time_str, '%Y-%m-%d')
        timestamp = int(time.mktime(time_array))

        return timestamp

    def update_database(self, response_text):
        json_str = self._get_json_str(response_text)

        my_json = json.loads(json_str)
        self._total_page = my_json['listInfo']['totalPages']

        insert_sql = 'insert into pdf(`stock_code`, `title`, `pdf_file`,\
                `create_date`) value (%d, "%s", "%s", %d)'
        for item in my_json['listInfo']['content']:
            my_insert_sql = insert_sql % (int(item['companyCd']), \
                    item['disclosureTitle'], item['destFilePath'],\
                    self.str_2_time(item['publishDate']))

            print my_insert_sql

            self._mysql_connect._cursor.execute(my_insert_sql)
        
        self._mysql_connect._conn.commit()
