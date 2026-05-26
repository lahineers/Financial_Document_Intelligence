from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.processing_status import (
    ProcessingStatus
)

from models.document import (
    Document
)

from schemas.processing_status import (
    ProcessingStatusCreate,
    ProcessingStatusUpdate
)


class ProcessingStatusService:
    """
    Handles processing status
    business logic.
    """


    @staticmethod
    def create_status(
        payload: ProcessingStatusCreate,
        db: Session
    ):
        """
        Create processing status.
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

        exists = db.query(
            ProcessingStatus
        ).filter(
            ProcessingStatus.doc_id
            ==
            payload.doc_id
        ).first()

        if exists:

            raise HTTPException(
                400,
                "Status already exists"
            )

        status = ProcessingStatus(
            **payload.model_dump()
        )

        db.add(
            status
        )

        db.commit()

        db.refresh(
            status
        )

        return status


    @staticmethod
    def get_statuses(
        db: Session
    ):
        """
        Fetch statuses.
        """

        return db.query(
            ProcessingStatus
        ).all()


    @staticmethod
    def get_status(
        doc_id,
        db: Session
    ):
        """
        Fetch status.
        """

        status = db.query(
            ProcessingStatus
        ).filter(
            ProcessingStatus.doc_id
            ==
            doc_id
        ).first()

        if not status:

            raise HTTPException(
                404,
                "Status not found"
            )

        return status


    @staticmethod
    def update_status(
        status,
        payload,
        db: Session
    ):
        """
        Update status.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                status,
                key,
                value
            )

        db.commit()

        db.refresh(
            status
        )

        return status


    @staticmethod
    def delete_status(
        status,
        db: Session
    ):
        """
        Delete status.
        """

        db.delete(
            status
        )

        db.commit()