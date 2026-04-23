from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.book_dto import BookModel, BookCreate
from app.db.database import get_db
from app.entity.models import BookEntity

router = APIRouter(tags=["Books RPC"])

@router.post("/getBook", response_model=BookModel)
def get_book_rpc(id: int, db: Session = Depends(get_db)):
    book = db.query(BookEntity).filter(BookEntity.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/createBook", response_model=BookModel)
def create_book_rpc(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookEntity(title=book.title, author=book.author)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book