from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from uuid import uuid4
from datetime import datetime

from db import Base


class ProcessingStatus(Base):
    """
    Stores document processing progress.
    """

    __tablename__ = "processing_status"

    status_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    doc_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "documents.doc_id"
        ),
        nullable=False,
        unique=True,
        index=True
    )

    status = Column(
        String,
        nullable=False
    )

    progress_percent = Column(
        Integer,
        nullable=False,
        default=0
    )

    message = Column(
        String,
        nullable=True
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )