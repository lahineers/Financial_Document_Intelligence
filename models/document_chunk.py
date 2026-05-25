from sqlalchemy import Column
from sqlalchemy import Text
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from uuid import uuid4
from datetime import datetime

from db import Base


class DocumentChunk(Base):
    """
    Stores document chunks
    extracted from uploaded
    financial documents.
    """

    __tablename__ = "document_chunks"

    chunk_id = Column(
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

    chunk_text = Column(
        Text,
        nullable=False
    )

    chunk_index = Column(
        Integer,
        nullable=False
    )

    page_number = Column(
        Integer,
        nullable=False
    )

    section_metadata = Column(
        JSONB,
        nullable=False,
        default={}
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )