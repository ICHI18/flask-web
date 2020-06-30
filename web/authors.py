from flask import (
    Blueprint,render_template,
    request,redirect,url_for
)
from web.bookdb import get_db

bp = Blueprint('authors',__name__)

@bp.route('/authors',methods=['GET'])
def all():
    db = get_db()
    alldata = db.execute('SELECT * FROM authors').fetchall()
    return render_template('authors/all.html',authors = alldata)

@bp.route('/authors/new',methods = ['GET','POST'])
def new():
    if request.method == 'POST':
        name = request.form['name']
        bio  = request.form['bio']
        db   = get_db()
        db.execute(
        "INSERT INTO authors (name,bio) VALUES (?,?)",
        (name,bio)
        )
        db.commit()
        return redirect(url_for('authors.all'))
    return render_template('authors/new.html')

@bp.route('/authors/show/<author_id>',methods = ['GET'])
def show(author_id):
    db = get_db()
    author = db.execute('SELECT * FROM authors where id = ?',author_id).fetchone()
    return render_template('authors/show.html',author = author)

@bp.route('/authors/delete/<author_id>',methods = ['GET'])
def delete(author_id):
    db = get_db()
    db.execute(
        "DELETE from authors where id = ?",author_id
    )
    db.commit()
    return redirect(url_for('authors.all'))

@bp.route('/authors/edit<author_id>',methods = ['GET','POST'])
def edit(author_id):
    db = get_db()
    if request.method == 'POST':
        name = request.form['name']
        bio  = request.form['bio']
        db.execute(
            "UPDATE authors SET name = ?,bio = ? where id = ?",
            (name,bio,author_id)
        )
        db.commit()
        return redirect(url_for('authors.all'))
    
    author = db.execute('SELECT * FROM authors where id = ?',author_id).fetchone()
    return render_template('authors/edit.html',author = author)