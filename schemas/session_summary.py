from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


ALLOWED_SUMMARIES = {

    "executive",

    "financial",

    "risk",

    "general"

}


ALLOWED_MODELS = {

    "gpt-4",

    "gpt-4o",

    "gemini-2.5-flash",

    "deepseek-r1"

    "nvidia-nim"

}


class SessionSummaryCreate(BaseModel):
    """
    Schema for creating
    session summaries.
    """

    session_id: UUID

    summary_type: str

    content: str = Field(
        min_length=20,
        max_length=50000
    )

    model_used: str

    combined_metrics: dict = {}

    doc_count: int = Field(
        ge=1
    )


    @field_validator(
        "summary_type"
    )
    @classmethod
    def validate_summary(
        cls,
        value
    ):

        if value not in ALLOWED_SUMMARIES:

            raise ValueError(
                "Invalid summary type"
            )

        return value


    @field_validator(
        "model_used"
    )
    @classmethod
    def validate_model(
        cls,
        value
    ):

        if value not in ALLOWED_MODELS:

            raise ValueError(
                "Unsupported model"
            )

        return value


class SessionSummaryResponse(BaseModel):
    """
    Returned session summary.
    """

    session_summary_id: UUID

    session_id: UUID

    summary_type: str

    content: str

    model_used: str

    combined_metrics: dict

    doc_count: int

    generated_at: datetime


    class Config:

        from_attributes = True