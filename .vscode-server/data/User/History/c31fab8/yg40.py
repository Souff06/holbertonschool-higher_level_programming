from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple d'utilisateurs enregistrés (pour la démonstration)
users = {
    "user1": "password1",
    "user2": "password2"
}
@app.route('/', methods=['POST'])
def index():
    return ('Welcome a 3chiriiiii')

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
    app.run(debug=True, host='0.0.0.0', port=5000)
