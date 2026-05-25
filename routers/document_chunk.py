from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.document import (
    Document
)

from models.document_chunk import (
    DocumentChunk
)

from schemas.document_chunk import (
    ChunkCreate,
    ChunkResponse
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

        document = db.query(
            Document
        ).filter(
            Document.doc_id
            ==
            payload.doc_id
        ).first()

        if not document:

            raise HTTPException(
                status_code=404,
                detail="Document not found"
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
    Fetch all document chunks.
    """

    try:

        chunks = db.query(
            DocumentChunk
        ).all()

        return chunks

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
    Fetch chunk by id.
    """

    try:

        chunk = db.query(
            DocumentChunk
        ).filter(
            DocumentChunk.chunk_id
            ==
            chunk_id
        ).first()

        if not chunk:

            raise HTTPException(
                status_code=404,
                detail="Chunk not found"
            )

        return chunk

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
    Delete document chunk.
    """

    try:

        chunk = db.query(
            DocumentChunk
        ).filter(
            DocumentChunk.chunk_id
            ==
            chunk_id
        ).first()

        if not chunk:

            raise HTTPException(
                status_code=404,
                detail="Chunk not found"
            )

        db.delete(
            chunk
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