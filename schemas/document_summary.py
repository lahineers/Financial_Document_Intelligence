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


class SummaryCreate(BaseModel):
    """
    Schema for creating
    summaries.
    """

    doc_id: UUID

    summary_type: str

    content: str = Field(
        min_length=20,
        max_length=50000
    )

    model_used: str

    key_metrics: dict = {}


    @field_validator(
        "summary_type"
    )
    @classmethod
    def validate_type(
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


class SummaryResponse(BaseModel):
    """
    Returned summary schema.
    """

    summary_id: UUID

    doc_id: UUID

    summary_type: str

    content: str

    model_used: str

    key_metrics: dict

    generated_at: datetime


    class Config:

        from_attributes = True