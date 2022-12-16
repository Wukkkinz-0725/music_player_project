from flask import Flask, Response, request
from song_comments_db import SongCommentsDB
import json

# Create the Flask application object.
application = Flask(__name__)
HOST = '0.0.0.0'
PORT = 8000

@application.route("/")
def main():
    return "Welcome to SongCommentsDB"

@application.route("/comments/query/<cid>", methods=["GET"])
def get_comment_by_id(cid):
    res = SongCommentsDB.get_by_comment_id(cid)
    if res:
        res['date'] = res['date'].strftime('%Y-%m-%d %H:%M:%S')
        return Response(json.dumps(res), status=200, content_type="application/json")
    else:
        return Response("Not Found", status=404, content_type="text/plain")

@application.route("/comments/create", methods=["POST"])
def create_comment():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongCommentsDB.create_comment(body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to create", status=400, content_type="text/plain")

@application.route("/comments/delete/<cid>", methods=["POST"])
def delete_by_comment_id(cid):
    res = SongCommentsDB.delete_by_comment_id(cid)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to delete", status=400, content_type="text/plain")
    
@application.route("/comments/update/<cid>", methods=["POST"])
def update_comment(cid):
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return Response('Content-Type Not Supported', status=400, content_type="text/plain")
    body = request.json
    res = SongCommentsDB.update_by_comment_id(cid, body)
    return Response(json.dumps(res), status=200, content_type="application/json") if res else Response("Fail to update", status=400, content_type="text/plain")

if __name__ == "__main__":
    SongCommentsDB.init_db()
    application.run(debug=True, host=HOST, port=PORT)