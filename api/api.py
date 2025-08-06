from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Book import Book, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])



@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())



@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    year_published = data.get('year_published')


    if not title or not author:
        return jsonify({"error": "Title and author are required"}), 400

    new_book = Book(title=title, author=author, year_published=year_published)
    db.session.add(new_book)
    db.session.commit()
    return jsonify(new_book.to_dict()), 201



if __name__ == '__main__':
    app.run(debug=True)
