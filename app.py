from flask import *
import sqlite3
import sys

#sys.path.insert(0, 'routes')

#import routes

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find_index")
def find():
    return render_template("find.html")

@app.route("/view_index")
def view():
    con = sqlite3.connect("nyc.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select employee.employee_id,employee_name,work_location_borough,base_salary_USD from employee INNER JOIN employee_details ON employee.employee_id=employee_details.employee_id limit 5")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/find_findID", methods=["POST", "GET"])
def find_id():
    con = sqlite3.connect("nyc.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    form_query = request.form["id"]
    cur.execute("select employee_id,employee_name FROM employee where employee_id ="+form_query)
    rows = cur.fetchall()
    return render_template("find_success.html", rows=rows)




if __name__ == "__main__":
    app.run(debug=True)
