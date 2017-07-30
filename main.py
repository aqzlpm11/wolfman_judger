from flask import Flask, send_file, render_template, request, redirect, session
from random import random
import socket

nxt_room_id = 1
rooms = {}

app = Flask(__name__)


@app.route('/')
def create_room():
    global nxt_room_id
    ret = nxt_room_id
    nxt_room_id += 1
    session.clear()
    return redirect('/enter_room?room_id=' + str(ret))


@app.route('/enter_room')
def enter_room():
    if 'user_id' in session:
        return redirect('/room')
    room_id = request.args.get('room_id')
    if room_id is None:
        room_id = ""
    else:
        room_id = "%03d" % (int(room_id))
    return render_template('enter_room.html', room_id=room_id)

def user_enter_room(room_id, user_id, username):
    global rooms
    if room_id not in rooms:
        rooms[room_id] = {}

    if 'users' not in rooms[room_id]:
        rooms[room_id]['users'] = []

    rooms[room_id]['users'].append([user_id, username])


@app.route('/enter_room_post', methods=["POST"])
def enter_room_post():
    room_id = request.form['room_id']
    user_id = request.form['user_id']
    username = request.form['username']

    session['room_id'] = room_id
    session['user_id'] = user_id
    session['username'] = username

    user_enter_room(room_id, user_id, username)

    return redirect('/room')


@app.route('/room')
def room():
    if 'user_id' not in session:
        return redirect('enter_room')
    msg = str([session['room_id'], session['user_id'], session['username']])
    msg += str(rooms)
    return render_template('room.html', room_id=session['room_id'], msg=msg)

# def _get_local_ip():
#     hostname = socket.gethostname()
#     ip = socket.gethostbyname(hostname)
#     return ip

if __name__ == '__main__':
    # ip = _get_local_ip()
    app.secret_key = 'lkbjasldmz98vj2k39aksnd21?L)1dKL'
    app.run("0.0.0.0", port=5000, threaded=True, debug=True)
