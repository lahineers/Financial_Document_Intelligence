from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.document import (
    Document
)

from models.document_summary import (
    DocumentSummary
)

from schemas.document_summary import (
    SummaryCreate,
    SummaryUpdate
)


class DocumentSummaryService:
    """
    Handles document summary
    business logic.
    """


    @staticmethod
    def create_summary(
        payload: SummaryCreate,
        db: Session
    ):
        """
        Create summary.
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

        summary = DocumentSummary(

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
            DocumentSummary
        ).all()


    @staticmethod
    def get_summary(
        doc_id,
        db: Session
    ):
        """
        Fetch summary.
        """

        summary = db.query(
            DocumentSummary
        ).filter(
            DocumentSummary.doc_id
            ==
            doc_id
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
        payload: SummaryUpdate,
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