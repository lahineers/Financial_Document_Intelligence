from pydantic import BaseModel
from pydantic import Field

from uuid import UUID
from datetime import datetime


class ChunkCreate(BaseModel):
    """
    Schema for creating
    document chunks.
    """

    doc_id: UUID

    chunk_text: str = Field(
        min_length=1,
        max_length=50000
    )

    chunk_index: int = Field(
        ge=0
    )

    page_number: int = Field(
        ge=1
    )

    section_metadata: dict = {}


class ChunkUpdate(BaseModel):
    """
    Schema for updating
    document chunks.
    """

    chunk_text: str | None = Field(
        default=None,
        min_length=1,
        max_length=50000
    )

    chunk_index: int | None = Field(
        default=None,
        ge=0
    )

    page_number: int | None = Field(
        default=None,
        ge=1
    )

    section_metadata: dict | None = None


class ChunkResponse(BaseModel):
    """
    Returned chunk schema.
    """

    chunk_id: UUID

    doc_id: UUID

    chunk_text: str

    chunk_index: int

    page_number: int

    section_metadata: dict

    created_at: datetime


    class Config:

        from_attributes = True