from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.document import (
    Document
)

from models.document_chunk import (
    DocumentChunk
)

from schemas.document_chunk import (
    ChunkCreate,
    ChunkUpdate
)


class DocumentChunkService:
    """
    Handles document chunk
    business logic.
    """


    @staticmethod
    def create_chunk(
        payload: ChunkCreate,
        db: Session
    ):
        """
        Create chunk.
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

        chunk = DocumentChunk(

            **payload.model_dump()

        )

        db.add(
            chunk
        )

        db.commit()

        db.refresh(
            chunk
        )

        return chunk


    @staticmethod
    def get_chunks(
        db: Session
    ):
        """
        Fetch chunks.
        """

        return db.query(
            DocumentChunk
        ).all()


    @staticmethod
    def get_chunk(
        chunk_id,
        db: Session
    ):
        """
        Fetch chunk.
        """

        chunk = db.query(
            DocumentChunk
        ).filter(
            DocumentChunk.chunk_id
            ==
            chunk_id
        ).first()

        if not chunk:

            raise HTTPException(
                404,
                "Chunk not found"
            )

        return chunk


    @staticmethod
    def update_chunk(
        chunk,
        payload: ChunkUpdate,
        db: Session
    ):
        """
        Update chunk.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                chunk,
                key,
                value
            )

        db.commit()

        db.refresh(
            chunk
        )

        return chunk


    @staticmethod
    def delete_chunk(
        chunk,
        db: Session
    ):
        """
        Delete chunk.
        """

        db.delete(
            chunk
        )

        db.commit()