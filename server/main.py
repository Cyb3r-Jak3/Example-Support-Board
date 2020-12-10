from flask import Blueprint, render_template, jsonify, request, url_for, redirect
from .models import adminUser, supportMember
import os
from . import db

main = Blueprint("main", __name__)

# with app.app_context():
#     test_user = adminUser()
#     test_user.username = "admin"
#     test_user.set_password("admin")
#     db.session.add(test_user)
#     db.session.commit()

@main.before_app_first_request
def load_people():
    main.people = supportMember.query.all()

@main.route('/')
def index():
    return render_template("index.html", people=supportMember.query.all())


@main.route("/api/admin/add/<string:user_type>", methods=["POST"])
def add_support(user_type: str):
    """

    :param user_type:
    :return:
    """
    if user_type not in {"support", "admin"}:
        return jsonify({"Error": "Bad user type"}), 400
    if user_type == "support":
        newTeammate = supportMember(request.form["fname"], request.form["lname"])
        db.session.add(newTeammate)
        db.session.commit()
        return "User Created"

    return ""


@main.route("/api/single/<name>", methods=["GET"])
def get_single(name):
    try:
        person_object = [x for x in main.people if x.personId == name][0]
    except IndexError:
        return jsonify({"Error": "Person not found"}), 404
    return jsonify(
        person_object.currentStatus()
    )


@main.route("/api/all", methods=["GET"])
def get_data():
    return jsonify([x.currentStatus() for x in main.people])
