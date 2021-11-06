from flask import Flask, request
from werkzeug.wrappers import response
app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

users_ONGs = {
    1: {
        "id": 1,
        "name": "LOVE"
    },
    2:{
        "id": 2,
        "name": "PEACE"
    } 
}

def response_users():
    return {"ongs": list(users_ONGs.values())}

@app.route("/")
def root():
    return "<hl>Cadastro de ONGS</hl>"

@app.route("/ongs")
def list_users():
    return response_users()

@app.route("/ongs", methods=["POST"])
def create_user():
    body = request.json
    ids = list(users_ONGs.keys())
    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1
    users_ONGs[new_id] = {
        "id": new_id,
        "name": body["name"]
    }
    return response_users ()

@app.route("/ongs/<int:user_id>", methods=["DELETE"])
def delete(user_id: int):
    user = users_ONGs.get(user_id)
    if user: 
        del users_ONGs[user_id]
    return response_users()

@app.route("/ongs/<int:user_id>", methods=["PUT"])
def update(user_id: int):
    body = request.json
    name = body.get("name")
    if user_id in users_ONGs:
        users_ONGs[user_id] ["name"] = name

    return response_users()




app.run(debug=True)