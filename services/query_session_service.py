from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.user import (
    User
)

from models.query_session import (
    QuerySession
)

from schemas.query_session import (
    QuerySessionCreate,
    QuerySessionUpdate
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

        user = db.query(
            User
        ).filter(
            User.user_id
            ==
            payload.user_id
        ).first()

        if not user:

            raise HTTPException(
                404,
                "User not found"
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
        """
        Fetch sessions.
        """

        return db.query(
            QuerySession
        ).all()


    @staticmethod
    def get_session(
        session_id,
        db: Session
    ):
        """
        Fetch session.
        """

        session = db.query(
            QuerySession
        ).filter(
            QuerySession.session_id
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
        payload: QuerySessionUpdate,
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