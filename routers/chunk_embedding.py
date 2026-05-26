from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.chunk_embedding import (
    EmbeddingCreate,
    EmbeddingResponse
)

from services.chunk_embedding_service import (
    ChunkEmbeddingService
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
    for document chunk.
    """

    try:

        return ChunkEmbeddingService.create_embedding(
            payload,
            db
        )

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

        return ChunkEmbeddingService.get_embeddings(
            db
        )

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
    by embedding id.
    """

    try:

        return ChunkEmbeddingService.get_embedding(
            embedding_id,
            db
        )

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

        embedding = (

            ChunkEmbeddingService
            .get_embedding(

                embedding_id,

                db

            )

        )

        ChunkEmbeddingService.delete_embedding(

            embedding,

            db

        )

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