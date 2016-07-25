from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")
@app.route("/application-form")
def application_page():
    """Show application form to user"""


    return render_template("application-form-complete.html")

@app.route("/application")
def application_confirmation():
    """once application is submitted, shows user the confirmation page"""

    firstname = request.args.get("firstname")
    lastname = request.args.get("lastname")
    jobs = request.args.get("jobs")
    salary = request.args.get ("salary")

    return render_template("application-response.html",
                            firstname = firstname,
                            lastname = lastname,
                            jobs = jobs,
                            salary = salary)









if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")

