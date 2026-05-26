from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from db import get_db

from schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse
)

from services.document_service import (
    DocumentService
)


router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_document(
    payload: DocumentCreate,
    db: Session = Depends(get_db)
):
    """
    Create document metadata.
    """

    try:

        return DocumentService.create_document(
            payload,
            db
        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[
        DocumentResponse
    ]
)
def get_documents(
    db: Session = Depends(get_db)
):
    """
    Get all documents.
    """

    try:

        return DocumentService.get_documents(
            db
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/{doc_id}",
    response_model=DocumentResponse
)
def get_document(
    doc_id: str,
    db: Session = Depends(get_db)
):
    """
    Fetch document by id.
    """

    try:

        return DocumentService.get_document(
            doc_id,
            db
        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.put(
    "/{doc_id}",
    response_model=DocumentResponse
)
def update_document(
    doc_id: str,
    payload: DocumentUpdate,
    db: Session = Depends(get_db)
):
    """
    Update document metadata.
    """

    try:

        document = DocumentService.get_document(
            doc_id,
            db
        )

        return DocumentService.update_document(
            document,
            payload,
            db
        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete(
    "/{doc_id}"
)
def delete_document(
    doc_id: str,
    db: Session = Depends(get_db)
):
    """
    Delete document.
    """

    try:

        document = DocumentService.get_document(
            doc_id,
            db
        )

        DocumentService.delete_document(
            document,
            db
        )

        return {

            "message":

            "Deleted"

        }

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )