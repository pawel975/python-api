from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
CORS(app)

user_post_args = reqparse.RequestParser()
user_post_args.add_argument(
    "username", type=str, help="Username is required", required=True
)
user_post_args.add_argument(
    "password", type=str, help="Password of the video is required", required=True
)

user_update_args = reqparse.RequestParser()
user_update_args.add_argument("username", type=str, help="Username is required")
user_update_args.add_argument(
    "password", type=str, help="Password of the video is required"
)

resource_fields = {
    "id": fields.Integer,
    "username": fields.String,
    "password": fields.String,
}


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Video(username = {self.username}, password = {self.password})"


class User(Resource):
    @marshal_with(resource_fields)
    def get(self, user_id):
        user = UserModel.query.filter_by(id=user_id)
        if not user:
            abort(404, message="Could not find video with that ID...")
        return user

    @marshal_with(resource_fields)
    def post(self, user_id):
        args = user_post_args.parse_args()
        result = UserModel.query.filter_by(id=user_id)
        if result:
            abort(409, message="User ID taken")
        user = UserModel(
            id=user_id, username=args["username"], password=args["password"]
        )
        db.session.add(user)
        db.session.commit()
        return user, 201

    @marshal_with(resource_fields)
    def patch(self, user_id):
        args = user_update_args.parse_args()
        user = UserModel.query.filter_by(id=user_id).first()
        if not user:
            abort(404, message="User doesn't exist, cannot update")

        if args["username"]:
            user.name = args["username"]
        if args["password"]:
            user.name = args["password"]

        db.session.commit()

    # TODO: Fix this method to work with db instead of non-existing object
    def delete(self, video_id):
        del videos[video_id]
        return "", 204


api.add_resource(User, "/user/<int:user_id>")

db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
