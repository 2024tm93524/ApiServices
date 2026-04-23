from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.book_dto import BookModel
from app.db.database import get_db
from app.entity.models import BookEntity

router = APIRouter(tags=["Books REST"])

@router.get("/books", response_model=list[BookModel])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(BookEntity).all()

@router.get("/books/{id}", response_model=BookModel)
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book = db.query(BookEntity).filter(BookEntity.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book