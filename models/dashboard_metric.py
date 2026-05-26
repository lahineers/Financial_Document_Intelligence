from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class DashboardMetric(Base):
    """
    Stores dashboard KPI metrics.
    """

    __tablename__ = "dashboard_metrics"

    metric_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    metric_name = Column(
        String,
        nullable=False,
        unique=True
    )

    metric_value = Column(
        Integer,
        nullable=False,
        default=0
    )

    metric_category = Column(
        String,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )