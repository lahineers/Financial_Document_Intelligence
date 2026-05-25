from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from uuid import uuid4
from datetime import datetime

from db import Base


class SessionSummary(Base):
    """
    Stores aggregated summaries
    generated across an
    upload session.
    """

    __tablename__ = "session_summaries"

    session_summary_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
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

    summary_type = Column(
        String(50),
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    model_used = Column(
        String(100),
        nullable=False
    )

    combined_metrics = Column(
        JSONB,
        nullable=False,
        default={}
    )

    doc_count = Column(
        Integer,
        nullable=False
    )

    generated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )