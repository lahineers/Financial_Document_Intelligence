from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.document import (
    Document
)

from models.document_summary import (
    DocumentSummary
)

from schemas.document_summary import (
    SummaryCreate
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

        return db.query(
            DocumentSummary
        ).all()


    @staticmethod
    def get_summary(
        summary_id,
        db: Session
    ):

        summary = db.query(
            DocumentSummary
        ).filter(
            DocumentSummary.summary_id
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
    def delete_summary(
        summary,
        db: Session
    ):

        db.delete(
            summary
        )

        db.commit()