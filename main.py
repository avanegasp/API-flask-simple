from flask import Flask, jsonify, request

app = Flask(__name__)

## Crear primer endpoint
@app.route('/')
def root():
    return "Hola"

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id == "0":
        response = {
            "error":"ID no válido",
            "message":"El ID proporcionado no es válido, por favor coloque el correcto"
        }
        return jsonify(response), 400
    
    if user_id != "123":
        response = {
            "error": "Uusario no encontrado",
            "message": f"el usuario con el ID {user_id} no se encuentra"
        }
        return jsonify(response),404
        
    user = {
        "id": user_id,
        "name": "Oliva",
        "phone": "3214556788"
    }
    return jsonify(user), 200

@app.route("/users", methods=['POST'])
def create_user():
    data =request.get_json()

    if data:
        return jsonify(data), 201
    else:
        return jsonify({"error": "No se recibieron los datos"}), 400    


if __name__ == '__main__':
    app.run(debug=True)
