import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data')
def get_data():
    data = {
        "name": "John Doe",
        "age": 30,
        "skills": ["Python", "React", "Flask"]
    }
    return jsonify(data)

@app.route('/api/profile')
def info_from_github():
    url = "https://api.github.com/users/rolandiartmeladze"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        profile_data = {
            "name": data.get("name"),
            "avatar": data.get("avatar_url"),
        }
        return jsonify(profile_data)
    else:
        return jsonify({"error": "not working"}), response.status_code

@app.route('/api/showposts')
def show_posts():
    try:
        with open('posts.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
      

@app.route('/api/posts', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()
        posts = []
        if os.path.exists('posts.json'):
            with open('posts.json', 'r') as f:
                posts = json.load(f)
        
        if not isinstance(posts, list):
            posts = [posts]

        posts.append(data)
        
        with open('posts.json', 'w') as f:
            json.dump(posts, f, indent=4)
            
        return jsonify({"message": "Data successfully saved"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
      
      
      

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
