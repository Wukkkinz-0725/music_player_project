import pymysql
import os
from datetime import datetime

class SongCommentsDB(object):

    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        conn = pymysql.connect(
            user="admin",
            password="dbuserbdbuser",
            host="e61561.cjmkumdiw0f0.us-east-1.rds.amazonaws.com",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def init_db():
        conn = SongCommentsDB.get_connection()
        drop_table_sql = "DROP TABLE IF EXISTS SongComments.comments"
        drop_db_sql = "DROP DATABASE IF EXISTS SongComments"
        db_sql = "CREATE DATABASE IF NOT EXISTS SongComments"
        table_sql = "CREATE TABLE IF NOT EXISTS SongComments.comments(cid integer AUTO_INCREMENT primary key, uid integer, username varchar(64), sid integer, content varchar(255), date datetime)"
        cur = conn.cursor()
        ret = cur.execute(drop_table_sql)
        ret = cur.execute(drop_db_sql)
        ret = cur.execute(db_sql)
        ret = cur.execute(table_sql)
        return ret

    @staticmethod
    def get_by_cid(cid):
        conn = SongCommentsDB.get_connection()
        sql = "SELECT * FROM SongComments.comments WHERE cid=%s"
        cur = conn.cursor()
        cur.execute(sql, args=cid)
        res = cur.fetchone()
        return res

    @staticmethod
    def get_by_sid(sid,limit,offset):
        conn = SongCommentsDB.get_connection()
        sql = "SELECT * FROM SongComments.comments WHERE sid=%s LIMIT %s OFFSET %s"
        cur = conn.cursor()
        args = (sid,limit,offset)
        cur.execute(sql, args)
        res = cur.fetchall()
        return res

    @staticmethod
    def get_by_uid(uid,limit,offset):
        conn = SongCommentsDB.get_connection()
        sql = "SELECT * FROM SongComments.comments WHERE uid=%s LIMIT %s OFFSET %s"
        cur = conn.cursor()
        args = (uid,limit,offset)
        cur.execute(sql, args)
        res = cur.fetchall()
        return res

    @staticmethod
    def create_comment(dic):

        cols = []
        place_holders = []
        values = []
        for k, v in dic.items():
            cols.append(k)
            place_holders.append("%s")
            values.append(v)
        
        sql = "INSERT INTO SongComments.comments (" + ",".join(cols) + ") VALUES (" + ",".join(place_holders) + ")"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)

        return ret

    @staticmethod
    def delete_by_cid(uid):
        sql = "DELETE FROM SongComments.comments WHERE cid=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=uid)
        return ret

    @staticmethod
    def delete_by_sid(sid):
        sql = "DELETE FROM SongComments.comments WHERE sid=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=sid)
        return ret

    @staticmethod
    def delete_by_uid(uid):
        sql = "DELETE FROM SongComments.comments WHERE uid=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=uid)
        return ret

    @staticmethod
    def update_by_cid(cid, dic):
        
        cols = []
        values = []
        for k, v in dic.items():
            cols.append(k + "=%s")
            values.append(v)
        
        values.append(cid)
        sql = "UPDATE SongComments.comments SET " + ",".join(cols) + " WHERE cid=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)
        return ret
    
    @staticmethod
    def update_by_uid(uid, dic):
        
        cols = []
        values = []
        for k, v in dic.items():
            cols.append(k + "=%s")
            values.append(v)
        
        values.append(uid)
        sql = "UPDATE SongComments.comments SET " + ",".join(cols) + " WHERE uid=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)
        return ret
