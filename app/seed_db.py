from app.db.database import SessionLocal, engine, Base
from app.entity.models import ArtistEntity, BookEntity

def seed_data():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    try:
        if db.query(ArtistEntity).count() == 0:
            print("Inserting 5 Indian Artists...")
            dummy_artists = [
                ArtistEntity(username="arrahman", name="A.R. Rahman", genre="Film Score", albums_published=150),
                ArtistEntity(username="rshankar", name="Ravi Shankar", genre="Indian Classical", albums_published=70),
                ArtistEntity(username="sghoshal", name="Shreya Ghoshal", genre="Playback Singing", albums_published=85),
                ArtistEntity(username="zhussain", name="Zakir Hussain", genre="Tabla / Classical", albums_published=60),
                ArtistEntity(username="lmangeshkar", name="Lata Mangeshkar", genre="Playback Singing", albums_published=200)
            ]
            db.add_all(dummy_artists)
        else:
            print("Artists already exist. Skipping.")

        if db.query(BookEntity).count() == 0:
            print("Inserting 5 Indian Music Books...")
            dummy_books = [
                BookEntity(title="Raga Mala: The Autobiography of Ravi Shankar", author="Ravi Shankar"),
                BookEntity(title="The Musical Heritage of India", author="M.R. Gautam"),
                BookEntity(title="A Rasika's Journey Through Hindustani Music", author="Rajeev Nair"),
                BookEntity(title="Bismillah Khan: The Maestro from Benaras", author="Juhi Sinha"),
                BookEntity(title="Lata Mangeshkar: In Her Own Voice", author="Nasreen Munni Kabir")
            ]
            db.add_all(dummy_books)
        else:
            print("Books already exist. Skipping.")

        db.commit()
        print("Database successfully seeded with 5 records each!")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_data()