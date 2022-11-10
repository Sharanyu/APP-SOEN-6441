from flask import *
from models.models import DBController


app = Flask(__name__,template_folder="../templates/")

obj=DBController()

@app.route("/")
def index():
    return render_template("index.html", )

@app.route("/find_index")
def find():
    return render_template("find.html")

@app.route("/find_emp_by_borough_index")
def filter():
    return render_template("borough.html")


@app.route("/borough_filter_borough", methods=["POST", "GET"])
def filter_borough():
    borough = request.form["borough"]
    rows= obj.view_emp_from(borough)
    #rows=UserController.find_emp(id)
    return render_template("borough_success.html", rows=rows)


@app.route("/view_index")
def view():
    rows= obj.view_emp()
    #emp_data=obj.find("employee")

    #rows=UserController.view_emp()
    return render_template("view.html", rows=rows)

@app.route("/find_findID", methods=["POST", "GET"])
def find_id():
    id = request.form["id"]
    rows= obj.find_emp(id)
    #rows=UserController.find_emp(id)
    return render_template("find_success.html", rows=rows)
