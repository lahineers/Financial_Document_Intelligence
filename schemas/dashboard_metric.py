from pydantic import BaseModel
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


VALID_CATEGORIES = {

    "documents",

    "reports",

    "queries",

    "processing"

}


class DashboardMetricBase(
    BaseModel
):

    metric_name: str

    metric_value: int

    metric_category: str

    @field_validator(
        "metric_value"
    )
    @classmethod
    def validate_value(
        cls,
        value
    ):

        if value < 0:

            raise ValueError(
                "Metric value cannot be negative"
            )

        return value

    @field_validator(
        "metric_category"
    )
    @classmethod
    def validate_category(
        cls,
        value
    ):

        if value not in VALID_CATEGORIES:

            raise ValueError(
                "Invalid category"
            )

        return value


class DashboardMetricCreate(
    DashboardMetricBase
):

    pass


class DashboardMetricUpdate(
    BaseModel
):

    metric_value: int | None = None


class DashboardMetricResponse(
    DashboardMetricBase
):

    metric_id: UUID

    updated_at: datetime

    model_config = {

        "from_attributes": True

    }