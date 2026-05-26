from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.upload_session import (
    UploadSession
)

from models.query_session import (
    QuerySession
)

from schemas.query_session import (
    QuerySessionCreate
)


class QuerySessionService:
    """
    Handles query session
    business logic.
    """


    @staticmethod
    def create_session(
        payload: QuerySessionCreate,
        db: Session
    ):
        """
        Create query session.
        """

        upload_session = db.query(
            UploadSession
        ).filter(
            UploadSession.session_id
            ==
            payload.upload_session_id
        ).first()

        if not upload_session:

            raise HTTPException(
                404,
                "Upload session not found"
            )

        session = QuerySession(
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

        return db.query(
            QuerySession
        ).all()


    @staticmethod
    def get_session(
        session_id,
        db: Session
    ):

        session = db.query(
            QuerySession
        ).filter(
            QuerySession.query_session_id
            ==
            session_id
        ).first()

        if not session:

            raise HTTPException(
                404,
                "Query session not found"
            )

        return session


    @staticmethod
    def delete_session(
        session,
        db: Session
    ):

        db.delete(
            session
        )

        db.commit()