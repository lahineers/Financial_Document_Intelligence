from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


ALLOWED_INSIGHT_TYPES = {

    "trend",

    "risk",

    "opportunity",

    "anomaly",

    "financial_health"

}


ALLOWED_SCOPE = {

    "document",

    "session"

}


ALLOWED_MODELS = {

    "gpt-4",

    "gpt-4o",

    "gemini-2.5-flash",

    "deepseek-r1"

    "nvidia-nim"

}


class InsightCreate(BaseModel):
    """
    Schema for creating
    insights.
    """

    doc_id: UUID

    session_id: UUID

    insight_text: str = Field(
        min_length=20,
        max_length=50000
    )

    insight_type: str

    model_used: str

    scope: str


    @field_validator(
        "insight_type"
    )
    @classmethod
    def validate_type(
        cls,
        value
    ):

        if value not in ALLOWED_INSIGHT_TYPES:

            raise ValueError(
                "Invalid insight type"
            )

        return value


    @field_validator(
        "scope"
    )
    @classmethod
    def validate_scope(
        cls,
        value
    ):

        if value not in ALLOWED_SCOPE:

            raise ValueError(
                "Invalid scope"
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


class InsightResponse(BaseModel):
    """
    Returned insight schema.
    """

    insight_id: UUID

    doc_id: UUID

    session_id: UUID

    insight_text: str

    insight_type: str

    model_used: str

    scope: str

    created_at: datetime


    class Config:

        from_attributes = True