from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from db import get_db

from schemas.upload_session import UploadSessionCreate
from schemas.upload_session import UploadSessionResponse
from schemas.upload_session import UploadSessionUpdate

from models.upload_session import UploadSession


router = APIRouter(
    prefix="/sessions",
    tags=["UploadSession"]
)


@router.post(
    "/",
    response_model=UploadSessionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_session(
    payload: UploadSessionCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new upload session.
    """

    try:

        session = UploadSession(
            user_id=payload.user_id,
            title=payload.title,
            status=payload.status
        )

        db.add(session)

        db.commit()

        db.refresh(session)

        return session

    except Exception:

        db.rollback()

        raise HTTPException(
            status_code=500,
            detail="Failed to create upload session"
        )


@router.get(
    "/",
    response_model=list[UploadSessionResponse]
)
def get_sessions(
    db: Session = Depends(get_db)
):
    """
    Fetch all upload sessions.
    """

    return db.query(
        UploadSession
    ).all()


@router.get(
    "/{session_id}",
    response_model=UploadSessionResponse
)
def get_session(
    session_id: str,
    db: Session = Depends(get_db)
):
    """
    Fetch upload session by id.
    """

    session = db.query(
        UploadSession
    ).filter(
        UploadSession.session_id == session_id
    ).first()

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    return session


@router.put(
    "/{session_id}",
    response_model=UploadSessionResponse
)
def update_session(
    session_id: str,
    payload: UploadSessionUpdate,
    db: Session = Depends(get_db)
):
    """
    Update upload session.
    """

    session = db.query(
        UploadSession
    ).filter(
        UploadSession.session_id == session_id
    ).first()

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    updates = payload.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():

        setattr(
            session,
            key,
            value
        )

    db.commit()

    db.refresh(session)

    return session


@router.delete(
    "/{session_id}"
)
def delete_session(
    session_id: str,
    db: Session = Depends(get_db)
):
    """
    Delete upload session.
    """

    session = db.query(
        UploadSession
    ).filter(
        UploadSession.session_id == session_id
    ).first()

    if not session:

        raise HTTPException(
            status_code=404,
            detail="Session not found"
        )

    db.delete(session)

    db.commit()

    return {
        "message": "Deleted successfully"
    }