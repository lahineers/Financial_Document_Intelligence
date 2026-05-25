from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class Insight(Base):
    """
    Stores AI generated
    financial insights.
    """

    __tablename__ = "insights"

    insight_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True
    )

    doc_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "documents.doc_id"
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

    insight_text = Column(
        Text,
        nullable=False
    )

    insight_type = Column(
        String(50),
        nullable=False
    )

    model_used = Column(
        String(100),
        nullable=False
    )

    scope = Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )