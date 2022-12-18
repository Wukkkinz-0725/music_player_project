import pymysql
import os
from datetime import datetime

class SongsDB(object):

    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        usr = 'admin'
        pw ="dbuserbdbuser"
        host = "e61561.cjmkumdiw0f0.us-east-1.rds.amazonaws.com"
        
        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=host,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def init_db(reset=False):
        # table info: sid, song_name, artist, release_date
        conn = SongsDB.get_connection()
        drop_table_songs_sql = "DROP TABLE IF EXISTS Songs.songs"
        drop_db_sql = "DROP DATABASE IF EXISTS Songs"
        db_sql = "CREATE DATABASE IF NOT EXISTS Songs"
        table_songs_sql = "CREATE TABLE IF NOT EXISTS Songs.songs(sid integer AUTO_INCREMENT primary key, song_name varchar(255), artist varchar(255), release_date Date)"
        cur = conn.cursor()
        if reset:
            cur.execute(drop_table_songs_sql)
            cur.execute(drop_db_sql)
        cur.execute(db_sql)
        cur.execute(table_songs_sql)

    @staticmethod
    def create_song(dic):
        cols = []
        place_holders = []
        values = []
        for k, v in dic.items():
            cols.append(k)
            place_holders.append("%s")
            values.append(v)
        
        sql = "INSERT INTO Songs.songs (" + ",".join(cols) + ") VALUES (" + ",".join(place_holders) + ")"
        conn = SongsDB.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=values)
        return res
    
    @staticmethod
    def delete_song_by_sid(uid):
        sql = "DELETE FROM Songs.songs WHERE sid=%s"
        conn = SongsDB.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=uid)
        return res

    @staticmethod
    def update_song_by_sid(sid, dic):
        cols = []
        values = []
        for k, v in dic.items():
            cols.append(k + "=%s")
            values.append(v)
        
        values.append(sid)
        sql = "UPDATE Songs.songs SET " + ",".join(cols) + " WHERE sid=%s"
        conn = SongsDB.get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=values)
        return res
    
    @staticmethod
    def get_all_songs(limit=20, offset=0):
        conn = SongsDB.get_connection()
        sql = "SELECT * FROM Songs.songs LIMIT %s OFFSET %s"
        args = (limit, offset)
        cur = conn.cursor()
        cur.execute(sql, args)
        res = cur.fetchall()
        return res
    
    @staticmethod
    def get_song_by_sid(id):
        conn = SongsDB.get_connection()
        sql = "SELECT * FROM Songs.songs WHERE sid=%s"
        cur = conn.cursor()
        cur.execute(sql, args=id)
        res = cur.fetchone()
        return res
    
    @staticmethod
    def get_songs_by_song_name(song_name, limit=20, offset=0):
        conn = SongsDB.get_connection()
        sql = "SELECT * FROM Songs.songs WHERE song_name=%s LIMIT %s OFFSET %s"
        cur = conn.cursor()
        args = (song_name, limit, offset)
        cur.execute(sql, args=args)
        res = cur.fetchall()
        return res