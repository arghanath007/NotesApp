from flask import Blueprint,render_template,request,flash,jsonify
from flask.helpers import flash
from flask_login import login_required,current_user
from website.models import Note
import json

from website import db

views=Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note=request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!!', category='error')
        else:
            new_note=Note(note=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Successfully Added Note!!', category='success')
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def deleteNote():
    note=json.loads(request.data)
    noteId=note['noteId']
    note=Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
