import os

from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from ....extensions import db, hcaptcha
from ...models import Contact

contact = Blueprint("contact", __name__)

@contact.route("/contact", methods=["GET", "POST"])
def contact_():
  if request.method == "POST":
    if hcaptcha.verify():
      name = request.form.get("name")
      email = request.form.get("email")
      message = request.form.get("message")
      new_contact = Contact(name=name, email=email, message=message)
      db.session.add(new_contact)
      db.session.commit()
      flash("Contact request sent!", "success")
      return redirect(url_for("home.home_")), 302
    else:
      flash("hCaptcha verification failed", "danger")
      return render_template("contact.html", site_key=os.getenv("HCAPTCHA_SITE_KEY")), 400

  elif request.method == "GET":
    return render_template("contact.html", site_key=os.getenv("HCAPTCHA_SITE_KEY")), 200
  else:
    abort(405)