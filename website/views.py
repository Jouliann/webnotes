from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .models import Dias
from . import db
import json
from datetime import datetime


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/dias', methods=['GET', 'POST'])
@login_required
def dias():
    if request.method == 'POST': 
        note = request.form.get('notedias')
        date = request.form.get('dateuser')
        datapy = datetime.strptime(date, '%Y-%m-%d').date() 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_dias = Dias(datadias=note, dateuser=datapy, user_id=current_user.id)  
            db.session.add(new_dias)
            db.session.commit()
            flash('Data adicionada', category='success')

    return render_template("dias.html", user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/delete-data', methods=['POST'])
def delete_data():  
    dia = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    diaId = dia['diaId']
    dia = Dias.query.get(diaId)
   
    if dia:
        if dia.user_id == current_user.id:
            db.session.delete(dia)
            db.session.commit()

    return jsonify({})
