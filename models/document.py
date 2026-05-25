from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import BigInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from uuid import uuid4
from datetime import datetime

from db import Base


class Document(Base):
    """
    Stores uploaded financial document metadata.

    Actual files are stored in cloud/object storage.
    Database stores metadata and processing state.
    """

    __tablename__ = "documents"

    doc_id = Column(
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

    session_id = Column(
        UUID(as_uuid=True),
        nullable=False,
        index=True
    )

    doc_type = Column(
        String(50),
        nullable=False
    )

    file_name = Column(
        String(255),
        nullable=False
    )

    file_type = Column(
        String(20),
        nullable=False
    )

    upload_time = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    document_path = Column(
        String(500),
        nullable=False
    )

    processing_status = Column(
        String(30),
        nullable=False,
        default="pending"
    )

    page_count = Column(
        Integer,
        nullable=False
    )

    file_size_bytes = Column(
        BigInteger,
        nullable=False
    )

    extracted_metadata = Column(
        JSONB,
        nullable=False,
        default={}
    )

    processed_at = Column(
        DateTime,
        nullable=True
    )