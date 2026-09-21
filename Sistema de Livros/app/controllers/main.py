from flask import Blueprint, render_template

from app.middleware import login_required


main_bp = Blueprint("main", __name__)


@main_bp.route("/home")
@login_required
def home():
    return render_template("home.html")