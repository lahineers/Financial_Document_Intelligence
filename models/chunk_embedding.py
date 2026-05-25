from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.dialects.postgresql import UUID

from pgvector.sqlalchemy import Vector

from uuid import uuid4
from datetime import datetime

from db import Base


class ChunkEmbedding(Base):
    """
    Stores vector embeddings
    generated from document chunks.
    """

    __tablename__ = "chunk_embeddings"

    embedding_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    chunk_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "document_chunks.chunk_id"
        ),
        nullable=False,
        index=True
    )

    embedding = Column(
        Vector(1536),
        nullable=False
    )

    model_name = Column(
        String,
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )