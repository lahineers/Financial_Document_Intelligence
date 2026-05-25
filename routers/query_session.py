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

from models.query_session import (
    QuerySession
)

from schemas.query_session import (
    QuerySessionCreate,
    QuerySessionResponse
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

        upload_session = db.query(
            UploadSession
        ).filter(
            UploadSession.session_id
            ==
            payload.upload_session_id
        ).first()

        if not upload_session:

            raise HTTPException(
                status_code=404,
                detail="Upload session not found"
            )

        query_session = QuerySession(
            **payload.model_dump()
        )

        db.add(
            query_session
        )

        db.commit()

        db.refresh(
            query_session
        )

        return query_session


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

        return db.query(
            QuerySession
        ).all()

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

    query_session = db.query(
        QuerySession
    ).filter(
        QuerySession.query_session_id
        ==
        query_session_id
    ).first()

    if not query_session:

        raise HTTPException(
            status_code=404,
            detail="Query session not found"
        )

    return query_session


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

        query_session = db.query(
            QuerySession
        ).filter(
            QuerySession.query_session_id
            ==
            query_session_id
        ).first()

        if not query_session:

            raise HTTPException(
                status_code=404,
                detail="Query session not found"
            )

        db.delete(
            query_session
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