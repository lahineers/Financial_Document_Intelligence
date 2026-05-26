from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.message import (
    MessageCreate,
    MessageResponse
)

from services.message_service import (
    MessageService
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

        return (

            MessageService
            .create_message(

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

        return (

            MessageService
            .get_messages(

                db

            )

        )

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

    try:

        return (

            MessageService
            .get_message(

                message_id,

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

        message = (

            MessageService
            .get_message(

                message_id,

                db

            )

        )

        MessageService.delete_message(

            message,

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