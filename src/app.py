from data import serial
from flask import Flask, request, send_file, render_template, session
from form import UserSchema
from flask_pydantic import validate
from operator import itemgetter
from dotenv import load_dotenv
from datetime import timedelta
import os

load_dotenv()

app = Flask(__name__) 
app.secret_key = os.getenv('SECRET_KEY')
app.permanent_session_lifetime = timedelta(minutes=2)

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
    username, email, age = itemgetter("username", "email", "age")(form.model_dump())
    return {"message": "Success", "data": {
        "name": username,
        "email": email,
        "age": age,
    }}, 201


if __name__=='__main__': 
   app.run(debug=True)