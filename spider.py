#!/usr/bin/env python
# encoding: utf-8

import requests
from parse import Parse
from config import COOKIE, PARAMS, BASE_URL, PROXY


class Spider(object):

    _cookie = None
    _parse = None

    def __init__(self):
        self._cookie = self._generate_cookies()

    def do_request(self):
        for params in self._generate_params():
            try:
                response = requests.post(BASE_URL, data=params, proxies=PROXY)
            except:
                self._log_miss_pdf(params)

            my_parse = Parse()
            my_parse.update_database(response.text)
            total_page = my_parse.get_total_page()
            if total_page > 1:
                self.do_next_request(params, total_page)

    def do_next_request(self, params, total_page):
        my_parse = Parse()
        for page in range(1, total_page + 1):
            try:
                params['page'] = page
                response = requests.post(BASE_URL, data=params, proxies=PROXY)
                my_parse.update_database(response.text)
            except:
                self._log_miss_pdf(params)

    def _log_miss_pdf(self, params):
        file_handler = open('miss_pdf.txt', 'w+')
        params = "%s\n" % params
        file_handler.write(params)
        file_handler.close()

    def _generate_params(self):
        date_string = '%s-%s-14'
        for year in range(2016, 2017):
            for month in range(6, 12):
                end_year = year
                if month == 0:
                    begin_year = year - 1
                    begin_month = 12
                    end_month = month + 1
                else:
                    begin_year = end_year
                    begin_month, end_month = month, month + 1

                begin_string = date_string % (str(begin_year),\
                                                str(begin_month).zfill(2))
                end_string = date_string % (str(end_year),\
                                                str(end_month).zfill(2))
                
                # user hump write style for the compatibility of request
                PARAMS['startTime'] = begin_string
                PARAMS['endTime'] = end_string

                yield PARAMS

    def _generate_cookies(self):
        '''
        generate python's request cookies with website's cookie @return type object
        '''
        my_cookie = COOKIE
        request_cookie = {}
        for line in my_cookie.split(';'):
            name, value = line.strip().split('=', 1)
            request_cookie[name] = value

        return request_cookie
