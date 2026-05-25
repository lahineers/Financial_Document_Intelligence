from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class UploadSession(Base):
    """
    Stores grouped upload sessions.
    One session can contain multiple documents.
    """

    __tablename__ = "upload_sessions"

    session_id = Column(
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

    title = Column(
        String(100),
        nullable=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="pending"
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    completed_at = Column(
        DateTime,
        nullable=True
    )