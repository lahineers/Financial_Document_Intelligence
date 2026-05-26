from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.query_session import (
    QuerySessionCreate,
    QuerySessionResponse
)

from services.query_session_service import (
    QuerySessionService
)


router = APIRouter(
    prefix="/query-sessions",
    tags=["QuerySession"]
)


@router.post(
    "/",
    response_model=QuerySessionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_query_session(
    payload: QuerySessionCreate,
    db: Session = Depends(get_db)
):
    """
    Create query session.
    """

    try:

        return (

            QuerySessionService
            .create_session(

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
        QuerySessionResponse
    ]
)
def get_query_sessions(
    db: Session = Depends(get_db)
):
    """
    Fetch query sessions.
    """

    try:

        return (

            QuerySessionService
            .get_sessions(

                db

            )

        )

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.get(
    "/{query_session_id}",
    response_model=QuerySessionResponse
)
def get_query_session(
    query_session_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch query session.
    """

    try:

        return (

            QuerySessionService
            .get_session(

                query_session_id,

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
    "/{query_session_id}"
)
def delete_query_session(
    query_session_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete query session.
    """

    try:

        query_session = (

            QuerySessionService
            .get_session(

                query_session_id,

                db

            )

        )

        QuerySessionService.delete_session(

            query_session,

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