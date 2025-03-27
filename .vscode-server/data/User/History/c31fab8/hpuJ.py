from flask import Flask, request, jsonify
from api.country_city_routes import country_city_routes
from .user_routes import user_routes

app = Flask(__name__)
app.register_blueprint(country_city_routes)
app.register_blueprint(user_routes)

@app.route('/test', methods=['POST'])
def test():
    data = request.json
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    app.run(debug=True)
