import strawberry
from strawberry.fastapi import GraphQLRouter
from app.db.database import SessionLocal
from app.entity.models import BookEntity

@strawberry.type
class BookType:
    id: int
    title: str
    author: str

@strawberry.type
class Query:
    @strawberry.field
    def book(self, id: int) -> BookType | None:
        db = SessionLocal()
        try:
            book_data = db.query(BookEntity).filter(BookEntity.id == id).first()
            if book_data:
                return BookType(id=book_data.id, title=book_data.title, author=book_data.author)
            return None
        finally:
            db.close()

# --- NEW: This handles creating data ---
@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> BookType:
        db = SessionLocal()
        try:
            new_book = BookEntity(title=title, author=author)
            db.add(new_book)
            db.commit()
            db.refresh(new_book) # Get the newly generated ID
            
            return BookType(id=new_book.id, title=new_book.title, author=new_book.author)
        finally:
            db.close()

# Make sure to register both Query and Mutation here!
schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)