from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.query_session import (
    QuerySession
)

from models.session_summary import (
    SessionSummary
)

from schemas.session_summary import (
    SessionSummaryCreate,
    SessionSummaryUpdate
)


class SessionSummaryService:
    """
    Handles session summary
    business logic.
    """


    @staticmethod
    def create_summary(
        payload: SessionSummaryCreate,
        db: Session
    ):
        """
        Create summary.
        """

        session = db.query(
            QuerySession
        ).filter(
            QuerySession.session_id
            ==
            payload.session_id
        ).first()

        if not session:

            raise HTTPException(
                404,
                "Session not found"
            )

        summary = SessionSummary(

            **payload.model_dump()

        )

        db.add(
            summary
        )

        db.commit()

        db.refresh(
            summary
        )

        return summary


    @staticmethod
    def get_summaries(
        db: Session
    ):
        """
        Fetch summaries.
        """

        return db.query(
            SessionSummary
        ).all()


    @staticmethod
    def get_summary(
        summary_id,
        db: Session
    ):
        """
        Fetch summary.
        """

        summary = db.query(
            SessionSummary
        ).filter(
            SessionSummary.summary_id
            ==
            summary_id
        ).first()

        if not summary:

            raise HTTPException(
                404,
                "Summary not found"
            )

        return summary


    @staticmethod
    def update_summary(
        summary,
        payload,
        db: Session
    ):
        """
        Update summary.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                summary,
                key,
                value
            )

        db.commit()

        db.refresh(
            summary
        )

        return summary


    @staticmethod
    def delete_summary(
        summary,
        db: Session
    ):
        """
        Delete summary.
        """

        db.delete(
            summary
        )

        db.commit()