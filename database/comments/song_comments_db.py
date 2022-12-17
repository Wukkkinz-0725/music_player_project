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
        table_sql = "CREATE TABLE IF NOT EXISTS SongComments.comments(comment_id integer AUTO_INCREMENT primary key, user_id integer, song_id integer, content varchar(255), date datetime)"
        cur = conn.cursor()
        ret = cur.execute(drop_table_sql)
        ret = cur.execute(drop_db_sql)
        ret = cur.execute(db_sql)
        ret = cur.execute(table_sql)
        return ret

    @staticmethod
    def get_by_comment_id(cid):
        conn = SongCommentsDB.get_connection()
        sql = "SELECT * FROM SongComments.comments WHERE comment_id=%s"
        cur = conn.cursor()
        cur.execute(sql, args=cid)
        res = cur.fetchone()
        return res

    @staticmethod
    def get_by_song_id(song_id,limit,offset):
        conn = SongCommentsDB.get_connection()
        sql = "SELECT * FROM SongComments.comments WHERE song_id=%s LIMIT %s OFFSET %s"
        cur = conn.cursor()
        args = (song_id,limit,offset)
        cur.execute(sql, args)
        res = cur.fetchall()
        return res

    @staticmethod
    def get_by_user_id(uid,limit,offset):
        conn = SongCommentsDB.get_connection()
        sql = "SELECT * FROM SongComments.comments WHERE user_id=%s LIMIT %s OFFSET %s"
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
    def delete_by_comment_id(uid):
        sql = "DELETE FROM SongComments.comments WHERE comment_id=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=uid)
        return ret

    @staticmethod
    def update_by_comment_id(comment_id, dic):
        
        cols = []
        values = []
        for k, v in dic.items():
            cols.append(k + "=%s")
            values.append(v)
        
        values.append(comment_id)
        sql = "UPDATE SongComments.comments SET " + ",".join(cols) + " WHERE comment_id=%s"
        conn = SongCommentsDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)
        return ret
