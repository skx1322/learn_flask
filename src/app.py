from flask import Flask, request, jsonify, send_file     
app = Flask(__name__) 

@app.route('/', methods=['GET'])       
def hello(): 
    filePath = '/public/FuHua27.png'
    if not filePath:
        print("Path not found.")
        return {"message": "Not found"}, 404
    
    return send_file(filePath, mimetype='image/jpeg')

@app.route("/book", methods=['GET'])
def log():
    return {"message": "Success", "data": "hello world"}, 200

@app.route("/book", methods=['POST'])
def book():
    username = request.form.get('username')
    return {"message": "Success", "data": username}, 201
  
if __name__=='__main__': 
   app.run(debug=True)