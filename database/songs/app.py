from flask import Flask, Response, request
from songs_db import SongsDB
from flask_cors import CORS
import os
import json

# Create the Flask application object.
songs_app = Flask(__name__)
CORS(songs_app)
songs_app.config['SECRET_KEY'] = 'whatever'

# functions for songs

@songs_app.route("/songs/create", methods=["POST"])
def create_song():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongsDB.create_song(body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to create", status=400, content_type="text/plain")
    
@songs_app.route("/songs/delete/<sid>", methods=["POST"])
def delete_song_by_sid(sid):
    res = SongsDB.delete_song_by_sid(sid)
    return Response("Successfully delete the songs", status=200, content_type="application/json") if res else Response("Cannot not find the sid {}. Fail to delete.".format(sid), status=400, content_type="text/plain")

@songs_app.route("/songs/update/<sid>", methods=["POST"])
def update_song(sid):
    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json':
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongsDB.update_song_by_sid(sid, body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Cannot not find the sid {}. Fail to update.".format(sid), status=400, content_type="text/plain")

@songs_app.route("/songs/query/sid/<sid>", methods=["GET"])
def get_song_by_id(sid):
    res = SongsDB.get_song_by_sid(sid)
    if res:
        res['release_date'] = res['release_date'].strftime('%Y-%m-%d')
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("There is no song with sid={}".format(sid), status=400, content_type="text/plain")

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
        return Response("There is no song with song_name={}".format(song_name), status=400, content_type="text/plain")
    
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
        return Response("There is no song.", status=400, content_type="text/plain")

if __name__ == "__main__":
    SongsDB.init_db()
    songs_app.run(host="0.0.0.0", port=8000)