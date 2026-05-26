from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class SavedQuery(Base):
    """
    Stores reusable AI queries.
    """

    __tablename__ = "saved_queries"

    saved_query_id = Column(
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

    query_text = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )