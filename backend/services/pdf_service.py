import fitz
import shutil
import uuid
from pathlib import Path

from fastapi import HTTPException, UploadFile


class PDFService:

    UPLOAD_DIR = Path("backend/uploads")
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def validate_pdf(file: UploadFile):

        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed."
            )

    @staticmethod
    def save_pdf(file: UploadFile):

        unique_filename = f"{uuid.uuid4()}.pdf"

        save_path = PDFService.UPLOAD_DIR / unique_filename

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return unique_filename, save_path

    @staticmethod
    def extract_document(pdf_path: str):

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        metadata = document.metadata

        result = {
            "title": metadata.get("title") or "Unknown",
            "author": metadata.get("author") or "Unknown",
            "subject": metadata.get("subject") or "Unknown",
            "keywords": metadata.get("keywords") or "Unknown",
            "pages": len(document),
            "characters": len(text),
            "text": text
        }

        document.close()

        return result