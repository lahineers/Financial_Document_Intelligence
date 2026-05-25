from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.chunk_embedding import (
    ChunkEmbedding
)

from models.document_chunk import (
    DocumentChunk
)

from schemas.chunk_embedding import (
    EmbeddingCreate,
    EmbeddingResponse
)


router = APIRouter(
    prefix="/embeddings",
    tags=["ChunkEmbedding"]
)


@router.post(
    "/",
    response_model=EmbeddingResponse,
    status_code=status.HTTP_201_CREATED
)
def create_embedding(
    payload: EmbeddingCreate,
    db: Session = Depends(get_db)
):
    """
    Create vector embedding
    for a document chunk.
    """

    try:

        chunk = db.query(
            DocumentChunk
        ).filter(
            DocumentChunk.chunk_id
            ==
            payload.chunk_id
        ).first()

        if not chunk:

            raise HTTPException(
                status_code=404,
                detail="Chunk not found"
            )

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

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/",
    response_model=list[
        EmbeddingResponse
    ]
)
def get_embeddings(
    db: Session = Depends(get_db)
):
    """
    Fetch all embeddings.
    """

    try:

        embeddings = db.query(
            ChunkEmbedding
        ).all()

        return embeddings

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/{embedding_id}",
    response_model=EmbeddingResponse
)
def get_embedding(
    embedding_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch embedding
    using embedding id.
    """

    try:

        embedding = db.query(
            ChunkEmbedding
        ).filter(
            ChunkEmbedding.embedding_id
            ==
            embedding_id
        ).first()

        if not embedding:

            raise HTTPException(
                status_code=404,
                detail="Embedding not found"
            )

        return embedding

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.delete(
    "/{embedding_id}"
)
def delete_embedding(
    embedding_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete embedding
    by embedding id.
    """

    try:

        embedding = db.query(
            ChunkEmbedding
        ).filter(
            ChunkEmbedding.embedding_id
            ==
            embedding_id
        ).first()

        if not embedding:

            raise HTTPException(
                status_code=404,
                detail="Embedding not found"
            )

        db.delete(
            embedding
        )

        db.commit()

        return {

            "message":

            "Deleted successfully"

        }

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )