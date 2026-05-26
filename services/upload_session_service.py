from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.upload_session import (
    UploadSession
)

from schemas.upload_session import (
    UploadSessionCreate,
    UploadSessionUpdate
)


class UploadSessionService:
    """
    Handles upload session
    business logic.
    """


    @staticmethod
    def create_session(
        payload: UploadSessionCreate,
        db: Session
    ):
        """
        Create upload session.
        """

        session = UploadSession(

            **payload.model_dump()

        )

        db.add(
            session
        )

        db.commit()

        db.refresh(
            session
        )

        return session


    @staticmethod
    def get_sessions(
        db: Session
    ):
        """
        Fetch sessions.
        """

        return db.query(
            UploadSession
        ).all()


    @staticmethod
    def get_session(
        session_id,
        db: Session
    ):
        """
        Fetch upload session.
        """

        session = db.query(
            UploadSession
        ).filter(
            UploadSession.session_id
            ==
            session_id
        ).first()

        if not session:

            raise HTTPException(
                404,
                "Session not found"
            )

        return session


    @staticmethod
    def update_session(
        session,
        payload: UploadSessionUpdate,
        db: Session
    ):
        """
        Update session.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                session,
                key,
                value
            )

        db.commit()

        db.refresh(
            session
        )

        return session


    @staticmethod
    def delete_session(
        session,
        db: Session
    ):
        """
        Delete session.
        """

        db.delete(
            session
        )

        db.commit()