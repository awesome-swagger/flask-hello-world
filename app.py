import sqlite3 as sql
from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/search")
def search():
  query = request.args.get('q')
  page = int(request.args.get('page') or 1) - 1
  URL = f"https://api.giphy.com/v1/gifs/search?limit=10{'&q='+query if not query == '' else '' }&offset={page*10}"
  PARAMS = { "api_key": "GxcROPu9p4Ai7eSk98Ks0EMrdjbtZ9nA" }
  r = requests.get(url=URL, params=PARAMS).json()
  re = [data["images"]["original"]["url"] for data in r["data"]]
  response = jsonify({"data": re, "pagination": r["pagination"]})
  response.headers.add('Access-Control-Allow-Origin', '*')
  return response

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
  app.run(host='0.0.0.0', port=5000, debug = True)
