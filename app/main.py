from fastapi import FastAPI
from app.api import artists_rest, books_rest, books_rpc
from app.api.books_graphql import graphql_app
from app.db.database import engine, Base
from app.entity import models

# Creates the database tables automatically on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Services", version="3.1.1")

app.include_router(artists_rest.router)
app.include_router(books_rest.router)
app.include_router(books_rpc.router)
#app.include_router(graphql_app, prefix="/graphql")
app.include_router(graphql_app, prefix="/graphql", tags=["Books GraphQL"])

@app.get("/")
def root():
    return {"message": "Welcome to api_services. Go to /docs for the Swagger UI."}