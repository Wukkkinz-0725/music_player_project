from flask import Flask, Response, request, render_template, url_for, flash, redirect
from songs_db import SongsDB
from flask_cors import CORS
from datetime import datetime
import os
import json

# Create the Flask application object.
songs_app = Flask(__name__)
CORS(songs_app)
songs_app.config['SECRET_KEY'] = 'whatever'

# functions for songs
@songs_app.route("/")
def main():
    data = SongsDB.get_all_songs()
    return render_template('songs.html', data=data)

@songs_app.route('/songs/detail/<sid>')
def view_songs_detail(sid):
    data = SongsDB.get_song_by_sid(sid)
    return render_template('song_detail.html', data=data)

@songs_app.route('/songs/new_songs', methods=('GET', 'POST'))
def create_songs_webpage():
    print('create song')
    if request.method == 'POST':
        # 在html里点击submit，会通过POST进入这个if statement
        songs_name = request.form['song_name']
        artist = request.form['artist']
        release_date = request.form['release_date']
        
        if not songs_name:
            flash('Song name is required!')
        elif not release_date:
            flash('Release date is required!')
        elif not artist:
            flash('Artist is required!')
        else:
            # 保存歌曲，并显示这首歌的detail
            res = SongsDB.create_song({'song_name': songs_name, 'artist': artist, 'release_date': release_date})
            return redirect(url_for('view_songs_detail', sid=res))
    # 点击create song button后直接渲染html
    return render_template('create_song.html')

@songs_app.route("/songs/create", methods=["POST"])
def create_song():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongsDB.create_song(body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to create", status=400, content_type="text/plain")

@songs_app.route('/songs/delete/<sid>')
def delete_song(sid):
    # TODO: delete this function and corresponding button
    delete_song_by_sid(sid)
    return redirect(url_for('main'))

@songs_app.route("/songs/delete/<sid>", methods=["POST"])
def delete_song_by_sid(sid):
    res = SongsDB.delete_song_by_sid(sid)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to delete", status=400, content_type="text/plain")

@songs_app.route('/songs/edit/<sid>', methods=('GET', 'POST'))
def edit_song_detail(sid):
    data = SongsDB.get_song_by_sid(sid)

    if request.method == 'POST':
        # 在html里点击submit，会通过POST进入这个if statement
        songs_name = request.form['song_name']
        artist = request.form['artist']
        release_date = request.form['release_date']

        if not songs_name:
            flash('Song name is required!')
        elif not artist:
            flash('Artist is required!')
        elif not release_date:
            flash('Release Date is required!')
        else:
            # 保存歌曲，并显示这首歌的detail
            SongsDB.update_song_by_sid(sid, {'song_name': songs_name, 'artist': artist, 'release_date': release_date})
            return redirect(url_for('view_songs_detail', sid=sid))
    # 点击edit song button后直接渲染html
    return render_template('edit_song_detail.html', data=data)

@songs_app.route("/songs/update/<sid>", methods=["POST"])
def update_song(sid):
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongsDB.update_song_by_sid(sid, body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to update", status=400, content_type="text/plain")

@songs_app.route("/songs/query/sid/<sid>", methods=["GET"])
def get_song_by_id(sid):
    res = SongsDB.get_song_by_sid(sid)
    if res:
        res['release_date'] = res['release_date'].strftime('%Y-%m-%d')
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("Not Found", status=404, content_type="text/plain")

@songs_app.route("/songs/query/song_name/<song_name>", methods=["GET"])
def get_songs_by_name(song_name):
    limit = request.args.get('limit', 20, type=int)
    offset = request.args.get('offset', 0, type=int)
    res = SongsDB.get_songs_by_song_name(song_name, limit=limit, offset=offset)
    if res:
        for r in res:
            r['release_date'] = r['release_date'].strftime('%Y-%m-%d')
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("Not Found", status=404, content_type="text/plain")
    
@songs_app.route("/songs/all", methods=["GET"])
def get_all_songs():
    limit = request.args.get('limit', 20, type=int)
    offset = request.args.get('offset', 0, type=int)
    res = SongsDB.get_all_songs(limit=limit, offset=offset)
    if res:
        for r in res:
            r['release_date'] = r['release_date'].strftime('%Y-%m-%d')
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("Not Found", status=404, content_type="text/plain")

if __name__ == "__main__":
    SongsDB.init_db(reset=True)
    port = int(os.environ.get('PORT', 9001))
    songs_app.run(host="localhost", port=port)