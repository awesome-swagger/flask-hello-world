import sqlite3 as sql
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

'''
@app.route('/post', methods = ['POST'])
def post():
  if request.method == 'POST':
    try:        
      with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO ... ")
        con.commit()
        msg = "Record successfully added"
    except:
        con.rollback()
        msg = "error in insert operation"
    finally:
        con.close()
        # return render_template("result.html", msg = msg)

@app.route('/list')
def list():
  con = sql.connect("database.db")
  con.row_factory = sql.Row

  cur = con.cursor()
  cur.execute("select * from students")

  rows = cur.fetchall();
  return render_template("list.html", rows = rows)
'''

if __name__ == "__main__":
  app.run(debug = True)
