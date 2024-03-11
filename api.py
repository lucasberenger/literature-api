from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)


@app.route('/books', methods=['GET'])
def get_books():
    table = pd.read_csv('BooksAPI.csv')
    books_list = table.to_dict(orient='records')
    return jsonify(books_list)
        

if __name__ == '__main__':
    app.run(port=5000,host='localhost',debug=True) 


