from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.document import (
    Document
)

from models.document_summary import (
    DocumentSummary
)

from schemas.document_summary import (
    SummaryCreate,
    SummaryResponse
)


router = APIRouter(
    prefix="/summaries",
    tags=["DocumentSummary"]
)


@router.post(
    "/",
    response_model=SummaryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_summary(
    payload: SummaryCreate,
    db: Session = Depends(get_db)
):
    """
    Create document summary.
    """

    try:

        document = db.query(
            Document
        ).filter(
            Document.doc_id
            ==
            payload.doc_id
        ).first()

        if not document:

            raise HTTPException(
                status_code=404,
                detail="Document not found"
            )

        summary = DocumentSummary(
            **payload.model_dump()
        )

        db.add(
            summary
        )

        db.commit()

        db.refresh(
            summary
        )

        return summary

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
        SummaryResponse
    ]
)
def get_summaries(
    db: Session = Depends(get_db)
):
    """
    Fetch summaries.
    """

    try:

        return db.query(
            DocumentSummary
        ).all()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/{summary_id}",
    response_model=SummaryResponse
)
def get_summary(
    summary_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch summary.
    """

    summary = db.query(
        DocumentSummary
    ).filter(
        DocumentSummary.summary_id
        ==
        summary_id
    ).first()

    if not summary:

        raise HTTPException(
            status_code=404,
            detail="Summary not found"
        )

    return summary


@router.delete(
    "/{summary_id}"
)
def delete_summary(
    summary_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete summary.
    """

    try:

        summary = db.query(
            DocumentSummary
        ).filter(
            DocumentSummary.summary_id
            ==
            summary_id
        ).first()

        if not summary:

            raise HTTPException(
                status_code=404,
                detail="Summary not found"
            )

        db.delete(
            summary
        )

        db.commit()

        return {

            "message":

            "Deleted successfully"

        }

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )