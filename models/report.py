from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class Report(Base):
    """
    Stores generated reports.
    """

    __tablename__ = "reports"

    report_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "users.user_id"
        ),
        nullable=False,
        index=True
    )

    session_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "upload_sessions.session_id"
        ),
        nullable=False,
        index=True
    )

    report_name = Column(
        String,
        nullable=False
    )

    report_type = Column(
        String,
        nullable=False
    )

    report_path = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False,
        default="pending"
    )

    generated_at = Column(
        DateTime,
        default=datetime.utcnow
    )