from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.session_summary import (
    SessionSummaryCreate,
    SessionSummaryResponse
)

from services.session_summary_service import (
    SessionSummaryService
)


router = APIRouter(
    prefix="/session-summaries",
    tags=["SessionSummary"]
)


@router.post(
    "/",
    response_model=SessionSummaryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_session_summary(
    payload: SessionSummaryCreate,
    db: Session = Depends(get_db)
):
    """
    Create session summary.
    """

    try:

        return (

            SessionSummaryService
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
        SessionSummaryResponse
    ]
)
def get_session_summaries(
    db: Session = Depends(get_db)
):
    """
    Fetch session summaries.
    """

    try:

        return (

            SessionSummaryService
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
    "/{session_summary_id}",
    response_model=SessionSummaryResponse
)
def get_session_summary(
    session_summary_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch session summary.
    """

    try:

        return (

            SessionSummaryService
            .get_summary(

                session_summary_id,

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
    "/{session_summary_id}"
)
def delete_session_summary(
    session_summary_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete session summary.
    """

    try:

        summary = (

            SessionSummaryService
            .get_summary(

                session_summary_id,

                db

            )

        )

        SessionSummaryService.delete_summary(

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