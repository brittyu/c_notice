#!/usr/bin/env python
# encoding: utf-8

# database configure
DBHOST = 'localhost'
DBUSER = 'root'
DBPWD = 'yxs'
DBPORT = 3306
DBNAME = 'root'
DBCHAR = 'utf8'
DBNAME = 'neeq_pdf'

# request header
HEADER = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }

# request proxy
PROXY = {
        'http': 'http://101.53.101.172:9999'
        }

# request base url
BASE_URL = 'http://www.neeq.com.cn/disclosureInfoController/infoResult.do?callback='


PARAMS = {
        'disclosureType': 5,
        'page': 2,
        'isNewThree': 1,
        'keyword': '关键字'
        }

# request cookie
COOKIE = 'Hm_lvt_b58fe8237d8d72ce286e1dbd2fc8308c=1481264542,1481510304,1481547155; Hm_lpvt_b58fe8237d8d72ce286e1dbd2fc8308c=1481547173'
