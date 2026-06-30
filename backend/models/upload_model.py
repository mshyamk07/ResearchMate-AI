from pydantic import BaseModel


class UploadResponse(BaseModel):
    message: str
    original_filename: str
    stored_filename: str
    saved_to: str

    title: str
    author: str

    doi: str
    publication_date: str
    abstract: str

    pages: int
    characters: int

    preview: str