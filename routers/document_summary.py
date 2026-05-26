from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.document_summary import (
    SummaryCreate,
    SummaryResponse
)

from services.document_summary_service import (
    DocumentSummaryService
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

        return (

            DocumentSummaryService
            .create_summary(

                payload,

                db

            )

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

        return (

            DocumentSummaryService
            .get_summaries(

                db

            )

        )

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

    try:

        return (

            DocumentSummaryService
            .get_summary(

                summary_id,

                db

            )

        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


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

        summary = (

            DocumentSummaryService
            .get_summary(

                summary_id,

                db

            )

        )

        DocumentSummaryService.delete_summary(

            summary,

            db

        )

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