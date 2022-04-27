import flask
import sqlite3

app = flask.Flask(__name__)

@app.route("/create", methods=['GET','POST'])
def create(): #URL: http://127.0.0.1:8001/create
    return flask.render_template("form.html")

@app.route("/create_submit", methods=['POST'])
def create_submit(): 
    first_name = flask.request.form['first_name']
    last_name = flask.request.form['last_name']
    position = flask.request.form['position']
    id = flask.request.form['id']

    con = sqlite3.connect('data/company.db')
    cur = con.cursor()
    cur.execute("INSERT INTO employees VALUES (?, ?, ?, ?)", (first_name, last_name, id, position))
    con.commit()
    return "Thank you for submitting the form"

@app.route("/view_all", methods=['GET', 'POST'])
def view_all(): #URL:http://127.0.0.1:8001/view_all
	db = []
	conn = sqlite3.connect('data/company.db')
	c = conn.cursor()
	fetchall = c.execute("SELECT * from employees")
	for element in (fetchall.fetchall()):
		db.append([element[0], element[1], element[2], element[3]])
	return flask.render_template('view.html', data = db)

if __name__ == '__main__':
	# Start the server
    app.run(port=8001, host='127.0.0.1', debug=True, use_evalex=False)