from pydantic import BaseModel, Field

class ArtistBase(BaseModel):
    name: str = Field(..., description="Artist name")
    genre: str = Field(..., description="Artist genre")
    albums_published: int = Field(..., description="Number of albums published under the label")

class ArtistCreate(ArtistBase):
    username: str = Field(..., description="Artist username")

class ArtistResponse(ArtistBase):
    username: str