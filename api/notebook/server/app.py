from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# Create a SQLite database connection
DATABASE_URL = "sqlite:///./notebook.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model
Base = declarative_base()

# Note model
class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)

# Create the database table
Base.metadata.create_all(bind=engine)

# FastAPI instance
app = FastAPI()

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new note
@app.post("/notes/", response_model=dict)
def create_note(title: str, content: str, db: Session = Depends(get_db)):
    note = Note(title=title, content=content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return {"message": "Note created successfully", "note": note.__dict__}

# Get all notes
@app.get("/notes/", response_model=list)
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    notes = db.query(Note).offset(skip).limit(limit).all()
    return notes

# Get a specific note
@app.get("/notes/{note_id}", response_model=dict)
def read_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note.__dict__

# Update a note
@app.put("/notes/{note_id}", response_model=dict)
def update_note(note_id: int, title: str = None, content: str = None, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    if title:
        note.title = title
    if content:
        note.content = content
    db.commit()
    db.refresh(note) # auto-incremented id or default values
    return {"message": "Note updated successfully", "note": note.__dict__}

# Delete a note
@app.delete("/notes/{note_id}", response_model=dict)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"message": "Note deleted successfully"}
