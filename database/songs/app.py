from flask import Flask, Response, request
from song_db import SongDB
import json

# Create the Flask application object.
song_app = Flask(__name__)
HOST = "localhost"
PORT = 9001

@song_app.route("/")
def main():
    return "Welcome to SongDB"

@song_app.route("/song/query/<cid>", methods=["GET"])
def get_song_by_id(cid):
    res = SongDB.get_by_song_id(cid)
    if res:
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("Not Found", status=404, content_type="text/plain")

@song_app.route("/song/create", methods=["POST"])
def create_song():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongDB.create_song(body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to create", status=400, content_type="text/plain")

@song_app.route("/song/delete/<cid>", methods=["POST"])
def delete_by_song_id(cid):
    res = SongDB.delete_by_song_id(cid)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to delete", status=400, content_type="text/plain")
    
@song_app.route("/song/update/<cid>", methods=["POST"])
def update_song(cid):
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongDB.update_by_song_id(cid, body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to update", status=400, content_type="text/plain")

if __name__ == "__main__":
    SongDB.init_db(reset=False)
    song_app.run(HOST, PORT)