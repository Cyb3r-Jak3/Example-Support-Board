"""Person Class"""
import random


def rand():
    return random.randint(0, 60)


class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        self.fullName = "{} {}".format(fname, lname)
        self.personId = "{}{}".format(fname.lower(), lname.title())
        self.chatAFR = rand()
        self.chats = rand()
        self.emails = rand()
        self.emailAFR = rand()
        self.calls = rand()
        self.phoneQueue = bool(random.getrandbits(1))
        self.chatQueue = bool(random.getrandbits(1))

    def __str__(self):
        return self.fullName

    def __repr__(self):
        return self.fullName

    def currentStatus(self) -> dict:
        return {
            "personId": self.personId,
            "chats": self.chats,
            "chatAFR": self.chatAFR,
            "emails": self.emails,
            "emailAFR": self.chatAFR,
            "calls": self.calls,
            "phoneStatus": self.phoneQueue,
            "chatStatus": self.chatQueue
        }