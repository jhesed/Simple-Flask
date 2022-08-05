import json
import uuid

from flask import jsonify, request, Flask

from models.user import User

app = Flask(__name__)


@app.get("/users")
def get_all_users():
    response = {
        "email": user.email for user in User.scan()
    }
    return jsonify(response)


@app.get("/users/<account_id>")
def get_user(account_id):
    try:
        return jsonify({"email": next(User.query(hash_key=account_id)).email})
    except StopIteration:
        return jsonify({})


@app.post("/users")
def create_user():
    data = json.loads(request.data)
    email = data.get("email")

    if not email:
        return jsonify({"err_code": "1234"}), 400

    account_id = str(uuid.uuid4())

    User(hash_key=account_id, email=email).save()
    return jsonify({"success": True}), 201


if __name__ == "__main__":
    app.run()
