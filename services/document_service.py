from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.document import (
    Document
)

from schemas.document import (
    DocumentCreate,
    DocumentUpdate
)


class DocumentService:
    """
    Handles document business logic.
    """


    @staticmethod
    def create_document(
        payload: DocumentCreate,
        db: Session
    ):
        """
        Create document.
        """

        document = Document(

            **payload.model_dump()

        )

        db.add(
            document
        )

        db.commit()

        db.refresh(
            document
        )

        return document


    @staticmethod
    def get_documents(
        db: Session
    ):
        """
        Fetch documents.
        """

        return db.query(
            Document
        ).all()


    @staticmethod
    def get_document(
        doc_id,
        db: Session
    ):
        """
        Fetch document.
        """

        document = db.query(
            Document
        ).filter(
            Document.doc_id
            ==
            doc_id
        ).first()

        if not document:

            raise HTTPException(
                404,
                "Document not found"
            )

        return document


    @staticmethod
    def update_document(
        document,
        payload: DocumentUpdate,
        db: Session
    ):
        """
        Update document.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                document,
                key,
                value
            )

        db.commit()

        db.refresh(
            document
        )

        return document


    @staticmethod
    def delete_document(
        document,
        db: Session
    ):
        """
        Delete document.
        """

        db.delete(
            document
        )

        db.commit()