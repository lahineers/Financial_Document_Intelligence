from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.saved_query import (
    SavedQueryCreate,
    SavedQueryUpdate,
    SavedQueryResponse
)

from services.saved_query_service import (
    SavedQueryService
)


router = APIRouter(
    prefix="/saved-queries",
    tags=["Saved Queries"]
)


@router.post(
    "/",
    response_model=SavedQueryResponse
)
def create_saved_query(
    payload: SavedQueryCreate,
    db: Session = Depends(get_db)
):
    """
    Create saved query.
    """

    try:

        return (
            SavedQueryService
            .create_query(
                payload,
                db
            )
        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            500,
            str(e)
        )


@router.get(
    "/",
    response_model=list[
        SavedQueryResponse
    ]
)
def get_saved_queries(
    db: Session = Depends(get_db)
):
    """
    Fetch saved queries.
    """

    try:

        return (
            SavedQueryService
            .get_queries(
                db
            )
        )

    except Exception as e:

        raise HTTPException(
            500,
            str(e)
        )


@router.get(
    "/{saved_query_id}",
    response_model=SavedQueryResponse
)
def get_saved_query(
    saved_query_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch saved query.
    """

    try:

        return (
            SavedQueryService
            .get_query(
                saved_query_id,
                db
            )
        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            500,
            str(e)
        )


@router.put(
    "/{saved_query_id}",
    response_model=SavedQueryResponse
)
def update_saved_query(
    saved_query_id: UUID,
    payload: SavedQueryUpdate,
    db: Session = Depends(get_db)
):
    """
    Update saved query.
    """

    try:

        query = (
            SavedQueryService
            .get_query(
                saved_query_id,
                db
            )
        )

        return (
            SavedQueryService
            .update_query(
                query,
                payload,
                db
            )
        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            500,
            str(e)
        )


@router.delete(
    "/{saved_query_id}"
)
def delete_saved_query(
    saved_query_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete saved query.
    """

    try:

        query = (
            SavedQueryService
            .get_query(
                saved_query_id,
                db
            )
        )

        SavedQueryService.delete_query(
            query,
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
            500,
            str(e)
        )