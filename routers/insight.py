from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.insight import (
    InsightCreate,
    InsightResponse
)

from services.insight_service import (
    InsightService
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

        return (

            InsightService
            .create_insight(

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

        return (

            InsightService
            .get_insights(

                db

            )

        )

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

    try:

        return (

            InsightService
            .get_insight(

                insight_id,

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

        insight = (

            InsightService
            .get_insight(

                insight_id,

                db

            )

        )

        InsightService.delete_insight(

            insight,

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