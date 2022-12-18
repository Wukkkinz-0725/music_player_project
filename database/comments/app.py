from flask import Flask, Response, request
from song_comment_db import SongCommentDB
import json

# Create the Flask application object.
comment_app = Flask(__name__)
HOST = "localhost"
PORT = 9001

@comment_app.route("/")
def main():
    return "Welcome to SongCommentDB"

@comment_app.route("/comment/query/<cid>", methods=["GET"])
def get_comment_by_id(cid):
    res = SongCommentDB.get_by_comment_id(cid)
    if res:
        res['date'] = res['date'].strftime('%Y-%m-%d %H:%M:%S')
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("Not Found", status=404, content_type="text/plain")

@comment_app.route("/comment/create", methods=["POST"])
def create_comment():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongCommentDB.create_comment(body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to create", status=400, content_type="text/plain")

@comment_app.route("/comment/delete/<cid>", methods=["POST"])
def delete_by_comment_id(cid):
    res = SongCommentDB.delete_by_comment_id(cid)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to delete", status=400, content_type="text/plain")
    
@comment_app.route("/comment/update/<cid>", methods=["POST"])
def update_comment(cid):
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongCommentDB.update_by_comment_id(cid, body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to update", status=400, content_type="text/plain")

if __name__ == "__main__":
    SongCommentDB.init_db(reset=False)
    comment_app.run(HOST, PORT)