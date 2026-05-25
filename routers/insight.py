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

from models.upload_session import (
    UploadSession
)

from models.insight import (
    Insight
)

from schemas.insight import (
    InsightCreate,
    InsightResponse
)


router = APIRouter(
    prefix="/insights",
    tags=["Insights"]
)


@router.post(
    "/",
    response_model=InsightResponse,
    status_code=status.HTTP_201_CREATED
)
def create_insight(
    payload: InsightCreate,
    db: Session = Depends(get_db)
):
    """
    Create insight.
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
                detail="Session not found"
            )

        insight = Insight(
            **payload.model_dump()
        )

        db.add(
            insight
        )

        db.commit()

        db.refresh(
            insight
        )

        return insight


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
        InsightResponse
    ]
)
def get_insights(
    db: Session = Depends(get_db)
):
    """
    Fetch insights.
    """

    try:

        return db.query(
            Insight
        ).all()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/{insight_id}",
    response_model=InsightResponse
)
def get_insight(
    insight_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch insight.
    """

    insight = db.query(
        Insight
    ).filter(
        Insight.insight_id
        ==
        insight_id
    ).first()

    if not insight:

        raise HTTPException(
            status_code=404,
            detail="Insight not found"
        )

    return insight


@router.delete(
    "/{insight_id}"
)
def delete_insight(
    insight_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete insight.
    """

    try:

        insight = db.query(
            Insight
        ).filter(
            Insight.insight_id
            ==
            insight_id
        ).first()

        if not insight:

            raise HTTPException(
                status_code=404,
                detail="Insight not found"
            )

        db.delete(
            insight
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