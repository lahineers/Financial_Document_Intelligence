from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator

from uuid import UUID
from datetime import datetime


ALLOWED_MODELS = {

    "text-embedding-3-small",

    "text-embedding-3-large",

    "bge-small",

    "bge-large"
}


class EmbeddingCreate(BaseModel):
    """
    Schema for creating embedding.
    """

    chunk_id: UUID

    embedding: list[float]

    model_name: str


    @field_validator(
        "embedding"
    )
    @classmethod
    def validate_embedding(
        cls,
        value
    ):

        if len(value) != 1536:

            raise ValueError(
                "Embedding dimension must be 1536"
            )

        return value


    @field_validator(
        "model_name"
    )
    @classmethod
    def validate_model(
        cls,
        value
    ):

        if value not in ALLOWED_MODELS:

            raise ValueError(
                "Invalid embedding model"
            )

        return value


class EmbeddingResponse(BaseModel):
    """
    Returned embedding schema.
    """

    embedding_id: UUID

    chunk_id: UUID

    embedding: list[float]

    model_name: str

    created_at: datetime


    class Config:

        from_attributes = True