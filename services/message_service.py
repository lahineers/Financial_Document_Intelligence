from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.query_session import (
    QuerySession
)

from models.message import (
    Message
)

from schemas.message import (
    MessageCreate,
    MessageUpdate
)


class MessageService:
    """
    Handles message
    business logic.
    """


    @staticmethod
    def create_message(
        payload: MessageCreate,
        db: Session
    ):
        """
        Create message.
        """

        session = db.query(
            QuerySession
        ).filter(
            QuerySession.query_session_id
            ==
            payload.query_session_id
        ).first()

        if not session:

            raise HTTPException(
                404,
                "Query session not found"
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


    @staticmethod
    def get_messages(
        db: Session
    ):
        """
        Fetch messages.
        """

        return db.query(
            Message
        ).all()


    @staticmethod
    def get_message(
        message_id,
        db: Session
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
                404,
                "Message not found"
            )

        return message


    @staticmethod
    def update_message(
        message,
        payload: MessageUpdate,
        db: Session
    ):
        """
        Update message.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                message,
                key,
                value
            )

        db.commit()

        db.refresh(
            message
        )

        return message


    @staticmethod
    def delete_message(
        message,
        db: Session
    ):
        """
        Delete message.
        """

        db.delete(
            message
        )

        db.commit()