from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.document import (
    Document
)

from models.insight import (
    Insight
)

from schemas.insight import (
    InsightCreate,
    InsightUpdate
)


class InsightService:
    """
    Handles insight
    business logic.
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
        """
        Fetch insights.
        """

        return db.query(
            Insight
        ).all()


    @staticmethod
    def get_insight(
        insight_id,
        db: Session
    ):
        """
        Fetch insight.
        """

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
    def update_insight(
        insight,
        payload: InsightUpdate,
        db: Session
    ):
        """
        Update insight.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                insight,
                key,
                value
            )

        db.commit()

        db.refresh(
            insight
        )

        return insight


    @staticmethod
    def delete_insight(
        insight,
        db: Session
    ):
        """
        Delete insight.
        """

        db.delete(
            insight
        )

        db.commit()