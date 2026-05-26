from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.upload_session import (
    UploadSession
)

from models.session_summary import (
    SessionSummary
)

from schemas.session_summary import (
    SessionSummaryCreate
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
        Create session summary.
        """

        session = db.query(
            UploadSession
        ).filter(
            UploadSession.session_id
            ==
            payload.session_id
        ).first()

        if not session:

            raise HTTPException(
                404,
                "Upload session not found"
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

        return db.query(
            SessionSummary
        ).all()


    @staticmethod
    def get_summary(
        summary_id,
        db: Session
    ):

        summary = db.query(
            SessionSummary
        ).filter(
            SessionSummary.session_summary_id
            ==
            summary_id
        ).first()

        if not summary:

            raise HTTPException(
                404,
                "Session summary not found"
            )

        return summary


    @staticmethod
    def delete_summary(
        summary,
        db: Session
    ):

        db.delete(
            summary
        )

        db.commit()