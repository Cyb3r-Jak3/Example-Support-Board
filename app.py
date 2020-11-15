from flask import Flask, request, render_template, jsonify, json
from shared import Person

app = Flask(__name__)

people = []


@app.before_first_request
def generate_people():
    for i in range(1, 9):
        people.append(Person("Person", str(i)))


@app.route('/')
def index():
    return render_template("index.html", people=people)


@app.route("/api/single/<name>", methods=["GET"])
def get_single(name):
    try:
        person_object = [x for x in people if x.personId == name][0]
    except IndexError:
        return jsonify({"Error": "Person not found"}), 404
    return jsonify(
        person_object.currentStatus()
    )


@app.route("/api/all", methods=["GET"])
def get_data():
    return jsonify([x.currentStatus() for x in people])


if __name__ == '__main__':
    app.run()
