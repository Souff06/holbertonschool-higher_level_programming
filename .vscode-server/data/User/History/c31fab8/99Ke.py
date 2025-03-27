from flask import Flask, request, jsonify
from api.country_city_routes import country_city_routes
from .user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(country_city_routes)
app.register_blueprint(user_routes)

@app.route('/')
def index():
    return 'Welcome to the Country and City API'

@app.route('/login', methods=['POST'])
def login():
    # Récupérer les données JSON de la requête
    data = request.json
    
    # Vérifier que les données JSON contiennent les champs 'username' et 'password'
    if 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password are required"}), 400

    username = data['username']
    password = data['password']
    
    # Vérifier les informations de connexion
    if username in users and users[username] == password:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

if __name__ == '__main__':
    app.run(debug=True)
