from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.query_session import (
    QuerySession
)

from models.message import (
    Message
)

from schemas.message import (
    MessageCreate,
    MessageResponse
)


router = APIRouter(
    prefix="/messages",
    tags=["Messages"]
)


@router.post(
    "/",
    response_model=MessageResponse,
    status_code=status.HTTP_201_CREATED
)
def create_message(
    payload: MessageCreate,
    db: Session = Depends(get_db)
):
    """
    Create message.
    """

    try:

        query_session = db.query(
            QuerySession
        ).filter(
            QuerySession.query_session_id
            ==
            payload.query_session_id
        ).first()

        if not query_session:

            raise HTTPException(
                status_code=404,
                detail="Query session not found"
            )

        message = Message(
            **payload.model_dump()
        )

        db.add(
            message
        )

        db.commit()

        db.refresh(
            message
        )

        return message


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
        MessageResponse
    ]
)
def get_messages(
    db: Session = Depends(get_db)
):
    """
    Fetch messages.
    """

    try:

        return db.query(
            Message
        ).all()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/{message_id}",
    response_model=MessageResponse
)
def get_message(
    message_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch message.
    """

    message = db.query(
        Message
    ).filter(
        Message.message_id
        ==
        message_id
    ).first()

    if not message:

        raise HTTPException(
            status_code=404,
            detail="Message not found"
        )

    return message


@router.delete(
    "/{message_id}"
)
def delete_message(
    message_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete message.
    """

    try:

        message = db.query(
            Message
        ).filter(
            Message.message_id
            ==
            message_id
        ).first()

        if not message:

            raise HTTPException(
                status_code=404,
                detail="Message not found"
            )

        db.delete(
            message
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