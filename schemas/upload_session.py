from pydantic import BaseModel
from pydantic import Field
from uuid import UUID
from datetime import datetime


class UploadSessionCreate(BaseModel):
    """
    Schema used when creating a new upload session.
    """

    user_id: UUID

    title: str = Field(
        min_length=3,
        max_length=100
    )

    status: str = Field(
        default="pending"
    )


class UploadSessionUpdate(BaseModel):
    """
    Schema used when updating upload session.
    """

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    status: str | None = None


class UploadSessionResponse(BaseModel):
    """
    Schema returned to client.
    """

    session_id: UUID

    user_id: UUID

    title: str

    status: str

    created_at: datetime

    completed_at: datetime | None

    class Config:
        from_attributes = True