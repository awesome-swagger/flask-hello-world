Hello World with Flask
======================

Step 1: Create and load your virtualenv::
------------------------
	virtualenv --no-site-packages venv 
	source venv/bin/activate

Step 2: Create your application in app.py::
------------------------
	import os
	from flask import Flask
	app = Flask(__name__)

	@app.route("/")
	def hello():
	  return "Hello World!"

	if __name__ == "__main__":
	  port = int(os.environ.get("PORT", 5000))
	  app.run(host='0.0.0.0', port=port)


Step 3: Run your application locally::
----------------------------
	python app.py
