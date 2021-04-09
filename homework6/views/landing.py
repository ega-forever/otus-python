from flask import Blueprint, render_template, jsonify, request
from loguru import logger
from models.contacts import Contact
from models.db import db

landing_app = Blueprint("landing_app", __name__)


@landing_app.route("/", methods=["GET"])
def index():
    return render_template("index.html", page="index")

@landing_app.route("/features", methods=["GET"])
def features():
    return render_template("features.html", page="features")

@landing_app.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html", page="contact")

@landing_app.route("/contact", methods=["POST"])
def contact_email():

    contact = Contact(
        mail=request.form.get('email'),
        subject=request.form.get('subject'),
        text=request.form.get('message')
    )

    db.session.add(contact)
    db.session.commit()

    logger.info('sent mail to email {}'.format(request.form.get('email')))
    return jsonify({
        "sent": 1,
    })