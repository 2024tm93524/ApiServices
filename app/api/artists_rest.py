from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.artist_dto import ArtistResponse, ArtistCreate
from app.core.security import verify_credentials
from app.db.database import get_db
from app.entity.models import ArtistEntity

router = APIRouter(prefix="/artists", tags=["Artists"])

@router.get("", response_model=List[ArtistResponse])
def get_artists(
    limit: int = Query(10, description="Amount of info on the page"),
    offset: int = Query(0, description="Page number/offset"),
    username: str = Depends(verify_credentials),
    db: Session = Depends(get_db) # Inject Database
):
    return db.query(ArtistEntity).offset(offset).limit(limit).all()

@router.post("", response_model=ArtistResponse, status_code=201)
def create_artist(
    artist: ArtistCreate, 
    username: str = Depends(verify_credentials),
    db: Session = Depends(get_db)
):
    # Check if user exists in DB
    existing_artist = db.query(ArtistEntity).filter(ArtistEntity.username == artist.username).first()
    if existing_artist:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Save to DB
    new_artist = ArtistEntity(**artist.model_dump())
    db.add(new_artist)
    db.commit()
    db.refresh(new_artist)
    return new_artist

@router.get("/{artistname}", response_model=ArtistResponse)
def get_artist_by_name(
    artistname: str, 
    username: str = Depends(verify_credentials),
    db: Session = Depends(get_db)
):
    # ilike handles case-insensitivity in SQLite
    artist = db.query(ArtistEntity).filter(ArtistEntity.name.ilike(artistname)).first()
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist