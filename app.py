from flask import Flask, send_from_directory, jsonify, request
import json

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/movie.html')
def movie():
    return send_from_directory('.', 'movie.html')

@app.route('/api/movies')
def get_movies():
    with open('data.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/movie')
def get_movie():
    movie_id = request.args.get('id')
    with open('data.json') as f:
        data = json.load(f)
    for movie in data:
        if movie['id'] == movie_id:
            return jsonify(movie)
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
