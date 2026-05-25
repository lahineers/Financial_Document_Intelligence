from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from db import get_db

from models.document import Document

from schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse
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

        document = Document(
            **payload.model_dump()
        )

        db.add(document)

        db.commit()

        db.refresh(document)

        return document

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Failed to create document"
        )


@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def get_documents(
    db: Session = Depends(get_db)
):
    """
    Get all documents.
    """

    return db.query(
        Document
    ).all()


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

    document = db.query(
        Document
    ).filter(
        Document.doc_id == doc_id
    ).first()

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document


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

    document = db.query(
        Document
    ).filter(
        Document.doc_id == doc_id
    ).first()

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    updates = payload.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():

        setattr(
            document,
            key,
            value
        )

    db.commit()

    db.refresh(document)

    return document


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

    document = db.query(
        Document
    ).filter(
        Document.doc_id == doc_id
    ).first()

    if not document:

        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    db.delete(document)

    db.commit()

    return {
        "message": "Deleted"
    }