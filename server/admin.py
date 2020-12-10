from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from flask_login import login_user, current_user
from .models import adminUser, supportMember
from .shared import is_safe_url

admin = Blueprint("admin", __name__)


@admin.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        if current_user.is_authenticated:
            return url_for("admin_dashboard")
        return render_template("admin_login.html")
    if request.method == "POST":
        print(request.form)
        form = request.form
        user = adminUser.query.filter_by(username=form.get("inputUser")).first_or_404()
        login_user(user)
        # if user.is_correct_password(form.get("password")):
        #     login_user(user)
        next_url = request.args.get('next')
        if not is_safe_url(next_url):
            return jsonify({"Error": "Bad UR:"}), 400

        return redirect(next_url or url_for("admin_dashboard"))


@admin.route("/admin/dashboard", methods=["GET"])
def admin_dashboard():
    print(supportMember.query.all())
    return render_template("admin_dashboard.html", people=supportMember.query.all())
