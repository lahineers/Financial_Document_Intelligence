from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.chunk_embedding import (
    ChunkEmbedding
)

from schemas.chunk_embedding import (
    EmbeddingCreate
)


class ChunkEmbeddingService:
    """
    Handles embedding business logic.
    """


    @staticmethod
    def create_embedding(
        payload: EmbeddingCreate,
        db: Session
    ):
        """
        Create embedding.
        """

        embedding = ChunkEmbedding(
            **payload.model_dump()
        )

        db.add(
            embedding
        )

        db.commit()

        db.refresh(
            embedding
        )

        return embedding


    @staticmethod
    def get_embeddings(
        db: Session
    ):
        """
        Fetch embeddings.
        """

        return db.query(
            ChunkEmbedding
        ).all()


    @staticmethod
    def get_embedding(
        embedding_id,
        db: Session
    ):
        """
        Fetch embedding.
        """

        embedding = db.query(
            ChunkEmbedding
        ).filter(
            ChunkEmbedding.embedding_id
            ==
            embedding_id
        ).first()

        if not embedding:

            raise HTTPException(
                404,
                "Embedding not found"
            )

        return embedding


    @staticmethod
    def delete_embedding(
        embedding,
        db: Session
    ):
        """
        Delete embedding.
        """

        db.delete(
            embedding
        )

        db.commit()