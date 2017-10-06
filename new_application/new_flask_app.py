
from flask import Flask, render_template
from flask import request
import requests
import json
app = Flask(__name__)
app.debug = True 

@app.route('/movie_search', methods = ['GET'])
def enter_movie():
	return render_template('movie_form.html')
@app.route('/omdb_data', methods = ['GET'])
def get_omdb_data():
	result = request.args
	favorite_mov= result.get('options')
	#print (favorite_mov)
	base_url = "https://itunes.apple.com/search?term=" 
	url = base_url + favorite_mov
	x = requests.get(url, params = {"media": "movie"}).text
	x = json.loads(x)["results"][0]["longDescription"]
	return render_template('movie_data.html', objects = x)

if __name__ == '__main__':
    app.run()