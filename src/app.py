from data import serial
from flask import Flask, request, send_file, render_template, session
from form import UserSchema
from flask_pydantic import validate
from operator import itemgetter
from dotenv import load_dotenv
from datetime import timedelta
import os
from model import db, UserModel

load_dotenv()

app = Flask(__name__) 
app.secret_key = os.getenv('SECRET_KEY')
app.permanent_session_lifetime = timedelta(minutes=2)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fuhua.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/", methods=['GET'])
def web():
    return render_template('index.html', title="Learn Flask", user_name="Nerdanta")

@app.route('/image/<filename>', methods=['GET'])       
def image(filename): 
    filePath = f'../public/{filename}'
    if not filePath:
        print("Path not found.")
        return {"message": "Not found"}, 404
    
    return send_file(filePath, mimetype='image/jpeg')

@app.route("/book", methods=['POST', 'GET'])
def log():
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user

        return {
            "message": "Success", 
            "data": f"Successfully login.",
            "book": user
        }, 200 
    else:
        if "user" in session: 
            query = request.args.get('name')
            right_book = [obj for obj in serial if obj['id'] == query]

            if not right_book:
                return {"message": "Not found"}, 404

            return {
                "message": "Success", 
                "data": f"Query: {query}.",
                "book": right_book
            }, 200
        return {
            "message": "Failed", 
            "data": f"User not login.",
        }, 401

@app.route("/logout", methods=['POST'])
def logout():
    session.pop("user", None)
    return {
    }, 204


@app.route("/create", methods=['POST'])
@validate(form=UserSchema)
def create_user(form: UserSchema):
    new_user = UserModel(
        username=form.username,
        email=form.email,
        # for learning purpose, there is no hashing at the moment
        password=form.password,
        age=form.age
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return {"message": "Success", "id": new_user.id}, 201
    except Exception as e:
        db.session.rollback()
        return {"message": "Database Error", "id": str(e)}, 500
    
@app.route("/user", methods=['GET'])
def get_user():
        # for learning purpose, there is no hashing at the moment
    users = UserModel.query.all()

    output = []
    for user in users:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "age": user.age
        }
        output.append(user_data)

    return {
        "message": "Success",
        "data": output,
        "total": len(output)
    }


if __name__=='__main__': 
   app.run(debug=True)