import pymysql
import os
from datetime import datetime

class SongDB(object):

    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        host = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user='root',
            password='dbuserdbuser',
            host=host,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def init_db(reset=False):
        # table info: song_id, song_name, album_name, singer
        conn = SongDB.get_connection()
        drop_table_sql = "DROP TABLE IF EXISTS Song.song_info"
        drop_db_sql = "DROP DATABASE IF EXISTS Song"
        db_sql = "CREATE DATABASE IF NOT EXISTS Song"
        table_sql = "CREATE TABLE IF NOT EXISTS Song.song_info(song_id integer primary key, song_name varchar(255), album_name varchar(255), singer varchar(255))"  
        cur = conn.cursor()
        if reset:
            ret = cur.execute(drop_table_sql)
            ret = cur.execute(drop_db_sql)
        ret = cur.execute(db_sql)
        ret = cur.execute(table_sql)
        return ret

    @staticmethod
    def get_all_songs():
        conn = SongDB.get_connection()
        sql = "SELECT * FROM Song.song_info"
        cur = conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        return res
    
    @staticmethod
    def get_by_song_id(id):
        conn = SongDB.get_connection()
        sql = "SELECT * FROM Song.song_info WHERE song_id=%s"
        cur = conn.cursor()
        cur.execute(sql, args=id)
        res = cur.fetchone()
        return res

    @staticmethod
    def create_song(dic):
        cols = []
        place_holders = []
        values = []
        for k, v in dic.items():
            cols.append(k)
            place_holders.append("%s")
            values.append(v)
        
        sql = "INSERT INTO Song.song_info (" + ",".join(cols) + ") VALUES (" + ",".join(place_holders) + ")"
        conn = SongDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)

        return ret

    @staticmethod
    def delete_by_song_id(uid):
        sql = "DELETE FROM Song.song_info WHERE song_id=%s"
        conn = SongDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=uid)
        return ret

    @staticmethod
    def update_by_song_id(song_id, dic):
        
        cols = []
        values = []
        for k, v in dic.items():
            cols.append(k + "=%s")
            values.append(v)
        
        values.append(song_id)
        sql = "UPDATE Song.song_info SET " + ",".join(cols) + " WHERE song_id=%s"
        conn = SongDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)
        return ret