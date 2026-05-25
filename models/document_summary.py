from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

from uuid import uuid4
from datetime import datetime

from db import Base


class DocumentSummary(Base):
    """
    Stores AI generated
    summaries for documents.
    """

    __tablename__ = "document_summaries"

    summary_id = Column(
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

    key_metrics = Column(
        JSONB,
        nullable=False,
        default={}
    )

    generated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow
    )