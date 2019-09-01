from flask import Flask , render_template
from index import out
import random

app = Flask(__name__)
links = out()

@app.route('/')
def displayImage():
	rad = random.randint(1,200)
	return render_template('index.html',linksOutput = links , randNum = rad)

if __name__ == '__main__':
	app.run(debug = True)
