from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


ALLOWED_ROLES = {

    "user",

    "assistant",

    "system"

}


class MessageCreate(BaseModel):
    """
    Schema for creating
    messages.
    """

    query_session_id: UUID

    role: str

    content: str = Field(
        min_length=1,
        max_length=50000
    )

    tool_calls: list = []

    source_chunks: list = []

    token_used: int = Field(
        ge=0
    )


    @field_validator(
        "role"
    )
    @classmethod
    def validate_role(
        cls,
        value
    ):

        if value not in ALLOWED_ROLES:

            raise ValueError(
                "Invalid role"
            )

        return value


class MessageResponse(BaseModel):
    """
    Returned message schema.
    """

    message_id: UUID

    query_session_id: UUID

    role: str

    content: str

    tool_calls: list

    source_chunks: list

    token_used: int

    created_at: datetime


    class Config:

        from_attributes = True