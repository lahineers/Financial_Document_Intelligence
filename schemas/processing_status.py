from pydantic import BaseModel
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


VALID_STATUS = {

    "pending",
    "uploading",
    "extracting",
    "chunking",
    "embedding",
    "summarizing",
    "completed",
    "failed"

}


class ProcessingStatusBase(
    BaseModel
):

    status: str

    progress_percent: int = 0

    message: str | None = None

    @field_validator(
        "status"
    )
    @classmethod
    def validate_status(
        cls,
        value
    ):

        if value not in VALID_STATUS:

            raise ValueError(
                "Invalid status"
            )

        return value

    @field_validator(
        "progress_percent"
    )
    @classmethod
    def validate_progress(
        cls,
        value
    ):

        if value < 0 or value > 100:

            raise ValueError(
                "Progress must be 0-100"
            )

        return value


class ProcessingStatusCreate(
    ProcessingStatusBase
):

    doc_id: UUID


class ProcessingStatusUpdate(
    BaseModel
):

    status: str | None = None

    progress_percent: int | None = None

    message: str | None = None

    @field_validator(
        "status"
    )
    @classmethod
    def validate_status(
        cls,
        value
    ):

        if value is None:

            return value

        if value not in VALID_STATUS:

            raise ValueError(
                "Invalid status"
            )

        return value


class ProcessingStatusResponse(
    ProcessingStatusBase
):

    status_id: UUID

    doc_id: UUID

    updated_at: datetime

    model_config = {

        "from_attributes": True

    }