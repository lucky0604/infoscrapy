# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
import datetime
import random
import app.settings as settings
from app.settings import (
    MYSQL_HOST,
    MYSQL_USER,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_DBNAME,
    CHARSET
)

class AppPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'info':

            host = MYSQL_HOST
            user = MYSQL_USER
            passwd = MYSQL_PASSWORD
            db = MYSQL_DBNAME
            port = MYSQL_PORT
            c = CHARSET

            con = pymysql.connect(
                host = host,
                user = user,
                passwd = passwd,
                db = db,
                charset = c,
                port = port
            )
            cue = con.cursor()
            print('mysql connect success')
            print(range(len(item)), ' --- item length ')
            print(len(item['product_name']))
            try:
                for i in range(len(item['product_name'])):
                    print(i, ' index i')
                    '''
                    cue.execute(
                        "insert into xl_product_demand (product_name, number, local_city_detail, need_city_detail, user_name, mobile, product_type, msg_type, create_time, local_city_id, need_city_id, user_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        [item['product_name'][i], item['num'][i], item['location'][i], item['destination'][i], '客服冉琳嘉', '18963800909', 2, 1, datetime.datetime.now(), random.randint(100000, 999999), random.randint(100000, 999999), 20180320193456525487]
                    )
                    '''
                    cue.execute(
                        "insert into info (product_name, num, location, destination, contact_user, contact_phone, product_type, msg_type, create_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        [item['product_name'][i], item['num'][i], item['location'][i], item['destination'][i], '客服孟岚', '15609911498', 2, 1, datetime.datetime.now()]
                    )

                print('insert success')
            except Exception as e:
                print('insert error', e)
                con.rollback()
            else:
                con.commit()
            con.close()
            return item
        elif spider.name == 'truckinfo':
            host = MYSQL_HOST
            user = MYSQL_USER
            passwd = MYSQL_PASSWORD
            db = MYSQL_DBNAME
            port = MYSQL_PORT
            c = CHARSET

            con = pymysql.connect(
                host = host,
                user = user,
                passwd = passwd,
                db = db,
                charset = c,
                port = port
            )
            cue = con.cursor()
            try:
                for i in range(len(item['product_name'])):
                    insertSql = "insert into info (product_name, num, location, destination, contact_user, contact_phone, product_type, msg_type, create_date) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    params = [item['num'][i], 1, item['location'][i], item['destination'][i], '客服孟岚', '15609911498', 1, 2, datetime.datetime.now()]
                    cue.execute(
                        insertSql,
                        params
                    )
                    ''' production
                    cue.execute(
                        "insert into xl_product_demand (product_name, number, local_city_detail, need_city_detail, user_name, mobile, product_type, msg_type, create_time, local_city_id, need_city_id, user_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        [item['num'][i], 1, item['location'][i], item['destination'][i], '客服冉琳嘉', '18963800909', 1, 2, datetime.datetime.now(), random.randint(100000, 999999), random.randint(100000, 999999), 20180320193456525487]
                    )
                    '''

                print('insert success')
            except Exception as e:
                print('insert error', e)
                con.rollback()
            else:
                con.commit()
            con.close()
            return item



