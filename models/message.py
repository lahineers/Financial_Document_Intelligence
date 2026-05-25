from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from uuid import uuid4
from datetime import datetime

from db import Base


class Message(Base):
    """
    Stores conversational
    messages belonging
    to query sessions.
    """

    __tablename__ = "messages"

    message_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        index=True
    )

    query_session_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "query_sessions.query_session_id"
        ),
        nullable=False,
        index=True
    )

    role = Column(
        String(20),
        nullable=False
    )

    content = Column(
        Text,
        nullable=False
    )

    tool_calls = Column(
        JSONB,
        nullable=False,
        default=[]
    )

    source_chunks = Column(
        JSONB,
        nullable=False,
        default=[]
    )

    token_used = Column(
        Integer,
        nullable=False
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )