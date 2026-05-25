from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


ALLOWED_FILE_TYPES = {
    "pdf",
    "xlsx",
    "xls"
}


ALLOWED_STATUS = {
    "pending",
    "extracting",
    "chunking",
    "embedding",
    "completed",
    "failed"
}


class DocumentCreate(BaseModel):
    """
    Schema for creating document.
    """

    user_id: UUID

    session_id: UUID

    doc_type: str = Field(
        min_length=2,
        max_length=50
    )

    file_name: str = Field(
        min_length=1,
        max_length=255
    )

    file_type: str = Field(
        min_length=2,
        max_length=20
    )

    document_path: str

    processing_status: str = "pending"

    page_count: int = Field(
        ge=0,
        le=100000
    )

    file_size_bytes: int = Field(
        gt=0
    )

    extracted_metadata: dict = {}

    processed_at: datetime | None = None


    @field_validator("file_type")
    @classmethod
    def validate_file_type(
        cls,
        value
    ):

        if value.lower() not in ALLOWED_FILE_TYPES:

            raise ValueError(
                "Only pdf/xlsx/xls allowed"
            )

        return value.lower()


    @field_validator(
        "processing_status"
    )
    @classmethod
    def validate_status(
        cls,
        value
    ):

        if value not in ALLOWED_STATUS:

            raise ValueError(
                "Invalid processing status"
            )

        return value


class DocumentUpdate(BaseModel):
    """
    Partial update schema.
    """

    doc_type: str | None = None

    processing_status: str | None = None

    page_count: int | None = None

    extracted_metadata: dict | None = None

    processed_at: datetime | None = None


class DocumentResponse(BaseModel):
    """
    Returned document response.
    """

    doc_id: UUID

    user_id: UUID

    session_id: UUID

    doc_type: str

    file_name: str

    file_type: str

    upload_time: datetime

    document_path: str

    processing_status: str

    page_count: int

    file_size_bytes: int

    extracted_metadata: dict

    processed_at: datetime | None

    class Config:

        from_attributes = True