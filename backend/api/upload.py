from backend.services.metadata_service import MetadataService
from backend.services.pdf_service import PDFService
from pathlib import Path
import shutil
import uuid
from fastapi import APIRouter, File, HTTPException, UploadFile
from backend.models.upload_model import UploadResponse
router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

# Upload folder
UPLOAD_DIR = Path("backend/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "/",
    response_model=UploadResponse,
    summary="Upload a research paper",
    description="Uploads a PDF, validates it, stores it securely, extracts metadata and returns a preview."
)
async def upload_pdf(file: UploadFile = File(...)):

    PDFService.validate_pdf(file)

    unique_filename, save_path = PDFService.save_pdf(file)

    document = PDFService.extract_document(str(save_path))
    metadata = MetadataService.extract(
    document["text"]
)
    return {
    "message": "PDF uploaded successfully.",
    "original_filename": file.filename,
    "stored_filename": unique_filename,
    "saved_to": str(save_path),

    "title": document["title"],
    "author": document["author"],

    "doi": metadata["doi"],
    "publication_date": metadata["publication_date"],
    "abstract": metadata["abstract"],

    "pages": document["pages"],
    "characters": document["characters"],
    "preview": document["text"][:500]
}