from flask import (
    Blueprint,render_template,request,redirect,url_for
)

from web.bookdb import get_db
bp = Blueprint('books',__name__)

@bp.route('/books',methods = ['GET'])
def all():
    db=get_db()
    alldata = db.execute('SELECT * FROM books').fetchall()
    return render_template('books/all.html',books=alldata)

@bp.route('/books/new',methods = ['GET','POST'])
def new():
    db = get_db()
    if request.method == 'POST':
        title  = request.form['title']
        author = request.form['author']
        db.execute(
            "INSERT INTO books (title,author) VALUES(?,?)",(title,author)
        )
        db.commit()
        return redirect(url_for('books.all'))
    
    authors = db.execute('SELECT * FROM authors').fetchall()
    return render_template('books/new.html',authors=authors)

@bp.route('/books/show/<book_id>',methods = ['GET'])
def show(book_id):
    db = get_db()
    book = db.execute('SELECT * FROM books where id = ?',book_id).fetchone()
    return render_template('books/show.html',book = book)

@bp.route('/books/upload/<book_id>',methods = ['GET','POST'])
def upload(book_id):
    db = get_db()
    book = db.execute('SELECT * FROM books where id = ?',book_id).fetchone()
    return render_template('books/upload.html',book = book)