from fastapi import FastAPI

from db import Base
from db import engine

from routers.upload_session import router

from models.upload_session import UploadSession
from routers.document import router as document_router
from models.document import Document
from routers.document_chunk import router as chunk_router

from routers.chunk_embedding import router as embedding_router
from models.chunk_embedding import ChunkEmbedding
from models.document_chunk import DocumentChunk
from routers.document_summary import router as summary_router
from routers.insight import router as insight_router
from models.insight import Insight

from routers.query_session import router as query_session_router
from models.query_session import QuerySession
from routers.message import router as message_router

from models.session_summary import SessionSummary
from routers.session_summary import router as session_summary_router

from models.user import User

from routers.user import router as user_router

from models.message import Message

from models.document_summary import DocumentSummary

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)
app.include_router(
    document_router
)
app.include_router(
    chunk_router
)
app.include_router(
    embedding_router
)
app.include_router(
    summary_router
)
app.include_router(
    insight_router
)
app.include_router(
    query_session_router
)
app.include_router(
    message_router
)
app.include_router(
    session_summary_router
)
app.include_router(
    user_router
)


@app.get("/")
def root():
    """
    Health check endpoint
    """
    return {
        "message": "Financial Doc API"
    }