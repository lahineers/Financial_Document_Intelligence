from pydantic import BaseModel
from pydantic import Field

from uuid import UUID
from datetime import datetime


class QuerySessionCreate(BaseModel):
    """
    Schema for creating
    query session.
    """

    user_id: UUID

    upload_session_id: UUID

    title: str = Field(
        min_length=3,
        max_length=255
    )


class QuerySessionResponse(BaseModel):
    """
    Returned query session.
    """

    query_session_id: UUID

    user_id: UUID

    upload_session_id: UUID

    title: str

    created_at: datetime

    updated_at: datetime | None


    class Config:

        from_attributes = True