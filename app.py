
from flask import Flask, jsonify, send_from_directory, request
import json
import os

# Initialize Flask app
app = Flask(__name__, static_folder='.', static_url_path='')

# Serve homepage
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Serve movie details page
@app.route('/movie.html')
def movie_page():
    return send_from_directory('.', 'movie.html')

# Serve full list of movies from data.json
@app.route('/api/movies')
def get_movies():
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    except:
        return jsonify([])

# Serve one specific movie by ID
@app.route('/api/movie')
def get_movie():
    movie_id = request.args.get('id')
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            movies = json.load(f)
        for movie in movies:
            if movie.get('id') == movie_id:
                return jsonify(movie)
        return jsonify({"error": "Movie not found"}), 404
    except:
        return jsonify({"error": "Data not found"}), 500

# Use correct host/port for Render
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
