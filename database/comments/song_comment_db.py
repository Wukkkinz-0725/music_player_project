import pymysql
import os

class SongCommentDB(object):

    def __init__(self):
        pass

    @staticmethod
    def get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        host = os.environ.get("DBHOST")

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
        conn = SongCommentDB.get_connection()
        drop_table_sql = "DROP TABLE IF EXISTS SongComment.comment"
        drop_db_sql = "DROP DATABASE IF EXISTS SongComment"
        db_sql = "CREATE DATABASE IF NOT EXISTS SongComment"
        table_sql = "CREATE TABLE IF NOT EXISTS SongComment.comment(comment_id integer primary key, user_id integer, song_id integer, content varchar(255), date datetime)"  
        cur = conn.cursor()
        if reset:
            ret = cur.execute(drop_table_sql)
            ret = cur.execute(drop_db_sql)
        ret = cur.execute(db_sql)
        ret = cur.execute(table_sql)
        return ret
    
    
    @staticmethod
    def get_by_comment_id(id):
        conn = SongCommentDB.get_connection()
        sql = "SELECT * FROM SongComment.comment WHERE comment_id=%s"
        cur = conn.cursor()
        cur.execute(sql, args=id)
        res = cur.fetchone()
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
        
        sql = "INSERT INTO SongComment.comment (" + ",".join(cols) + ") VALUES (" + ",".join(place_holders) + ")"
        conn = SongCommentDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)

        return ret

    @staticmethod
    def delete_by_comment_id(uid):
        sql = "DELETE FROM SongComment.comment WHERE comment_id=%s"
        conn = SongCommentDB.get_connection()
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
        sql = "UPDATE SongComment.comment SET " + ",".join(cols) + " WHERE comment_id=%s"
        conn = SongCommentDB.get_connection()
        cur = conn.cursor()
        ret = cur.execute(sql, args=values)
        return ret