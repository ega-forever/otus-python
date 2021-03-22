from flask import Blueprint, render_template, jsonify, request
from loguru import logger

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

    logger.info('sent mail to email {}'.format(request.form.get('email')))
    return jsonify({
        "sent": 1,
    })

# @product_app.route("/add/", methods=["GET", "POST"], endpoint="add")
# def product_add():
#     if request.method == "GET":
#         d_values = PRODUCTS.values()
#         last_element_name = tuple(d_values)[-1]
#         return render_template("products/add-new.html", last_element_name=last_element_name)
#
#     PRODUCTS[next(next_index)] = request.form.get("product-name")
#     return redirect(url_for("product_app.list"))