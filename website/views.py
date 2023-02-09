from flask import Blueprint, render_template
from product_database import get_products

views = Blueprint("views", __name__)

@views.route("/", methods= ["GET", "POST"])
def home():
    return render_template("home.html", title = 'Home', result=get_products("Fruits"))



