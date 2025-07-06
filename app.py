from flask import Flask, jsonify, send_from_directory, request
import json, os

app = Flask(__name__, static_folder="../frontend/assets", template_folder="../frontend")

@app.route('/')
def index():
    return send_from_directory(app.template_folder, 'index.html')

@app.route('/movie.html')
def movie():
    return send_from_directory(app.template_folder, 'movie.html')

@app.route('/api/movies')
def get_movies():
    with open("backend/data.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/api/movie')
def get_movie():
    movie_id = request.args.get("id")
    with open("backend/data.json") as f:
        data = json.load(f)
    for movie in data:
        if movie["id"] == movie_id:
            return jsonify(movie)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
