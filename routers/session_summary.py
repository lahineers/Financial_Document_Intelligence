from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.upload_session import (
    UploadSession
)

from models.session_summary import (
    SessionSummary
)

from schemas.session_summary import (
    SessionSummaryCreate,
    SessionSummaryResponse
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

        session = db.query(
            UploadSession
        ).filter(
            UploadSession.session_id
            ==
            payload.session_id
        ).first()

        if not session:

            raise HTTPException(
                status_code=404,
                detail="Upload session not found"
            )

        summary = SessionSummary(
            **payload.model_dump()
        )

        db.add(
            summary)

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

        return db.query(
            SessionSummary
        ).all()

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

    summary = db.query(
        SessionSummary
    ).filter(
        SessionSummary.session_summary_id
        ==
        session_summary_id
    ).first()

    if not summary:

        raise HTTPException(
            status_code=404,
            detail="Session summary not found"
        )

    return summary


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

        summary = db.query(
            SessionSummary
        ).filter(
            SessionSummary.session_summary_id
            ==
            session_summary_id
        ).first()

        if not summary:

            raise HTTPException(
                status_code=404,
                detail="Session summary not found"
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