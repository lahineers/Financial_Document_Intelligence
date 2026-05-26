from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.document_chunk import (
    ChunkCreate,
    ChunkResponse
)

from services.document_chunk_service import (
    DocumentChunkService
)


router = APIRouter(
    prefix="/chunks",
    tags=["DocumentChunk"]
)


@router.post(
    "/",
    response_model=ChunkResponse,
    status_code=status.HTTP_201_CREATED
)
def create_chunk(
    payload: ChunkCreate,
    db: Session = Depends(get_db)
):
    """
    Create document chunk.
    """

    try:

        return (

            DocumentChunkService
            .create_chunk(

                payload,

                db

            )

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
        ChunkResponse
    ]
)
def get_chunks(
    db: Session = Depends(get_db)
):
    """
    Fetch all chunks.
    """

    try:

        return (

            DocumentChunkService
            .get_chunks(

                db

            )

        )

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.get(
    "/{chunk_id}",
    response_model=ChunkResponse
)
def get_chunk(
    chunk_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch chunk.
    """

    try:

        return (

            DocumentChunkService
            .get_chunk(

                chunk_id,

                db

            )

        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.delete(
    "/{chunk_id}"
)
def delete_chunk(
    chunk_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete chunk.
    """

    try:

        chunk = (

            DocumentChunkService
            .get_chunk(

                chunk_id,

                db

            )

        )

        DocumentChunkService.delete_chunk(

            chunk,

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