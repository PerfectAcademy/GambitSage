import json, os
from os.path import basename
from sqlalchemy.orm.exc import NoResultFound
from functools import wraps
from werkzeug.security import generate_password_hash,check_password_hash
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
from flask import * 
from flask_socketio import SocketIO, emit, join_room, leave_room
from markupsafe import escape
import re 
from flask_wtf.csrf import CSRFProtect
from file import app,csrf,socketio
from file.forms import *
from flask_login import login_required
from file.models import db,Contact
from file import mail
from flask_mail import Message

from sqlalchemy import func
from datetime import datetime
@app.route("/", methods=['GET', 'POST'])
def Homepage():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            contact_name=form.name.data,
            contact_email=form.email.data,
            contact_message=form.message.data,
            contact_no=form.phone.data
        )
        db.session.add(contact)
        db.session.commit()

        msg = Message('New Contact Form Submission', sender='carryoby@gmail.com', recipients=['carryoby@gmail.com'])
        msg.body = f'Name: {form.name.data}\nEmail: {form.email.data}\nPhone: {form.phone.data}\nMessage: {form.message.data}'
        mail.send(msg)

        flash(f"Your message has been sent. Thank you!", "success")
        return redirect(url_for('Homepage'))

    return render_template("index.html", form=form, pagename="Homepage | Cybersage")


