# importing required libraries
from flask import *
from models.models import dbc

# Initialising the flask object
app = Flask(__name__, template_folder="../views/")



# route to render the index.html
@app.route("/")
def index():
    return render_template(
        "index.html",
    )

# route to render the view.html
@app.route("/view_index")
def view():
    rows = dbc.view_emp()
    return render_template("view.html", rows=rows)


# route to render the find.html
@app.route("/find_index")
def find():
    return render_template("find.html")

# route to render the find_success.html
@app.route("/find_findID", methods=["POST", "GET"])
def find_id():
    id = request.form["id"]
    rows = dbc.find_emp(id)
    return render_template("find_success.html", rows=rows)


# route to render the top_earners.html
@app.route("/top_earners")
def top_earners():
    return render_template("top_earners.html")

# route to render the earners_success.html
@app.route("/top_earners_filter", methods=["POST", "GET"])
def top_earners_filter():
    year = request.form["year"]
    rows = dbc.top_5_earners(year)
    # rows=UserController.find_emp(id)
    return render_template("earners_success.html", rows=rows)


# route to render the borough.html
@app.route("/find_emp_by_borough_index")
def filter():
    return render_template("borough.html")

# route to render the borough_success.html
@app.route("/borough_filter_borough", methods=["POST", "GET"])
def filter_borough():
    borough = request.form["borough"]
    rows = dbc.view_emp_from(borough)
    return render_template("borough_success.html", rows=rows)





