from data import book_data, serial

from flask import Flask, request, send_file     
app = Flask(__name__) 

@app.route('/<filename>', methods=['GET'])       
def hello(filename): 
    filePath = f'../public/{filename}'
    if not filePath:
        print("Path not found.")
        return {"message": "Not found"}, 404
    
    return send_file(filePath, mimetype='image/jpeg')

@app.route("/book", methods=['GET'])
def log():
    query = request.args.get('name')
    right_book = [obj for obj in serial if obj['id'] == query]

    if not right_book:
        return {"message": "Not found"}, 404

    return {
        "message": "Success", 
        "data": f"Query: {query}",
        "book": right_book
    }, 200

@app.route("/book", methods=['POST'])
def book():
    username = request.form.get('username')
    return {"message": "Success", "data": username}, 201
  
if __name__=='__main__': 
   app.run(debug=True)