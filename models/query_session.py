from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class QuerySession(Base):
    """
    Stores conversational
    query sessions for
    financial intelligence.
    """

    __tablename__ = "query_sessions"

    query_session_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True
    )

    user_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True
    )

    upload_session_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "upload_sessions.session_id"
        ),
        nullable=False,
        index=True
    )

    title = Column(
        String(255),
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        nullable=True
    )