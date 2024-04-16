from flask import Flask, render_template, request, redirect
from models import Note, session

def create_app():
    app = Flask(__name__)

    # get all notes
    @app.get("/")
    def notes():
        notes_query = session.query(Note).all()
        notes = []
        for note in notes_query:
            notes.append({"id": note.id, "text": note.text})
        return render_template("notes.html", notes=notes)
    
    # create note
    @app.post("/new")
    def add_note():
        form = request.form
        session.add(Note(text=form['text']))
        session.commit()
        return redirect("/")
    
    # update note
    @app.post("/update")
    def update_note():
        form = request.form
        note = session.query(Note).filter_by(id=form['id']).first()
        note.text = form['text']
        session.commit()
        return redirect("/")
    
    # delete note
    @app.post("/delete")
    def delete_note():
        form = request.form
        print(form)
        note = session.query(Note).filter_by(id=form['id']).delete()
        session.commit()
        return redirect("/")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8080)