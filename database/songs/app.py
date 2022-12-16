from flask import Flask, Response, request, render_template, url_for, flash, redirect
from song_db import SongDB
import json

# Create the Flask application object.
song_app = Flask(__name__)
song_app.config['SECRET_KEY'] = 'whatever'
HOST = "localhost"
PORT = 9001

@song_app.route("/")
def main():
    data = SongDB.get_all_songs()
    return render_template('songs.html', data=data)

@song_app.route('/song/detail/<cid>')
def view_song_detail(cid):
    data = SongDB.get_by_song_id(cid)
    return render_template('song_detail.html', data=data)

@song_app.route('/song/new_song', methods=('GET', 'POST'))
def create_song_webpage():
    if request.method == 'POST':
        song_id = request.form['song_id']
        song_name = request.form['song_name']
        album_name = request.form['album_name']
        singer = request.form['singer']

        if not song_id:
            flash('Song ID is required!')  # TODO: flash is not working porperly
        elif not song_name:
            flash('Song name is required!')
        elif not album_name:
            flash('Album name is required!')
        elif not singer:
            flash('Singer is required!')
        else:
            SongDB.create_song({'song_id': song_id, 'song_name': song_name, 'album_name': album_name, 'singer': singer})
            return redirect(url_for('view_song_detail', cid=song_id))
    return render_template('create_song.html')

@song_app.route('/song/delete/<cid>')
def delete_song(cid):
    delete_by_song_id(cid)
    return redirect(url_for('main'))

@song_app.route('/song/edit/<cid>', methods=('GET', 'POST'))
def edit_song_detail(cid):
    data = SongDB.get_by_song_id(cid)

    if request.method == 'POST':
        song_id = request.form['song_id']
        song_name = request.form['song_name']
        album_name = request.form['album_name']
        singer = request.form['singer']

        if not song_id:
            flash('Song ID is required!')  # TODO: flash is not working porperly
        elif not song_name:
            flash('Song name is required!')
        elif not album_name:
            flash('Album name is required!')
        elif not singer:
            flash('Singer is required!')
        else:
            SongDB.update_by_song_id(cid, {'song_id': song_id, 'song_name': song_name, 'album_name': album_name, 'singer': singer})
            return redirect(url_for('view_song_detail', cid=song_id))
    return render_template('edit_song_detail.html', data=data)

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