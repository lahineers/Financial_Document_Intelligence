from pydantic import BaseModel
from pydantic import Field

from uuid import UUID
from datetime import datetime


class SavedQueryBase(
    BaseModel
):

    query_text: str = Field(
        min_length=3,
        max_length=500
    )

    description: str | None = Field(
        default=None,
        max_length=1000
    )


class SavedQueryCreate(
    SavedQueryBase
):

    user_id: UUID


class SavedQueryUpdate(
    BaseModel
):

    query_text: str | None = None

    description: str | None = None


class SavedQueryResponse(
    SavedQueryBase
):

    saved_query_id: UUID

    user_id: UUID

    created_at: datetime

    model_config = {

        "from_attributes": True

    }