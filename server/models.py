from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import random
from . import db


class supportMember(db.Model):
    __tablename__ = "supportMembers"
    personId = db.Column(db.String, unique=True, primary_key=True)
    chats = db.Column(db.INTEGER)
    chatAFR = db.Column(db.INTEGER)
    emails = db.Column(db.INTEGER)
    emailAFR = db.Column(db.INTEGER)
    calls = db.Column(db.INTEGER)
    photoPath = db.Column(db.String)

    def __init__(self, fname, lname):
        self.personId = "{}{}".format(fname.lower(), lname.title())

    def phoneQueue(self):
        return bool(random.getrandbits(1))

    def chatQueue(self):
        return bool(random.getrandbits(1))

    def currentStatus(self) -> dict:
        return {
            "personId": self.personId,
            "chats": self.chats,
            "chatAFR": self.chatAFR,
            "emails": self.emails,
            "emailAFR": self.chatAFR,
            "calls": self.calls,
            "phoneStatus": self.phoneQueue(),
            "chatStatus": self.chatQueue()
        }


class adminUser(UserMixin, db.Model):
    __tablename__ = "adminUsers"
    id = db.Column(db.String, unique=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
