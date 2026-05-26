from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.document import (
    Document
)

from models.upload_session import (
    UploadSession
)

from models.insight import (
    Insight
)

from schemas.insight import (
    InsightCreate
)


class InsightService:
    """
    Handles insight business logic.
    """


    @staticmethod
    def create_insight(
        payload: InsightCreate,
        db: Session
    ):
        """
        Create insight.
        """

        document = db.query(
            Document
        ).filter(
            Document.doc_id
            ==
            payload.doc_id
        ).first()

        if not document:

            raise HTTPException(
                404,
                "Document not found"
            )

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
                "Session not found"
            )

        insight = Insight(
            **payload.model_dump()
        )

        db.add(
            insight
        )

        db.commit()

        db.refresh(
            insight
        )

        return insight


    @staticmethod
    def get_insights(
        db: Session
    ):

        return db.query(
            Insight
        ).all()


    @staticmethod
    def get_insight(
        insight_id,
        db: Session
    ):

        insight = db.query(
            Insight
        ).filter(
            Insight.insight_id
            ==
            insight_id
        ).first()

        if not insight:

            raise HTTPException(
                404,
                "Insight not found"
            )

        return insight


    @staticmethod
    def delete_insight(
        insight,
        db: Session
    ):

        db.delete(
            insight
        )

        db.commit()