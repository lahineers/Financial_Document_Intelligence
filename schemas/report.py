from pydantic import BaseModel
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


VALID_TYPES = {

    "financial",

    "summary",

    "insight",

    "custom"

}


VALID_STATUS = {

    "pending",

    "generating",

    "completed",

    "failed"

}


class ReportBase(
    BaseModel
):

    report_name: str

    report_type: str

    report_path: str

    status: str = "pending"

    @field_validator(
        "report_type"
    )
    @classmethod
    def validate_type(
        cls,
        value
    ):

        if value not in VALID_TYPES:

            raise ValueError(
                "Invalid report type"
            )

        return value

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


class ReportCreate(
    ReportBase
):

    user_id: UUID

    session_id: UUID


class ReportUpdate(
    BaseModel
):

    report_name: str | None = None

    report_path: str | None = None

    status: str | None = None


class ReportResponse(
    ReportBase
):

    report_id: UUID

    user_id: UUID

    session_id: UUID

    generated_at: datetime

    model_config = {

        "from_attributes": True

    }