from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.processing_status import (
    ProcessingStatusCreate,
    ProcessingStatusUpdate,
    ProcessingStatusResponse
)

from services.processing_status_service import (
    ProcessingStatusService
)


router = APIRouter(
    prefix="/processing-status",
    tags=["Processing Status"]
)


@router.post(
    "/",
    response_model=ProcessingStatusResponse,
    status_code=status.HTTP_201_CREATED
)
def create_status(
    payload: ProcessingStatusCreate,
    db: Session = Depends(get_db)
):
    """
    Create processing status.
    """

    try:

        return (

            ProcessingStatusService
            .create_status(

                payload,

                db

            )

        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.get(
    "/",
    response_model=list[
        ProcessingStatusResponse
    ]
)
def get_statuses(
    db: Session = Depends(get_db)
):
    """
    Fetch statuses.
    """

    try:

        return (

            ProcessingStatusService
            .get_statuses(

                db

            )

        )

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.get(
    "/{doc_id}",
    response_model=ProcessingStatusResponse
)
def get_status(
    doc_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch document status.
    """

    try:

        return (

            ProcessingStatusService
            .get_status(

                doc_id,

                db

            )

        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.put(
    "/{doc_id}",
    response_model=ProcessingStatusResponse
)
def update_status(
    doc_id: UUID,
    payload: ProcessingStatusUpdate,
    db: Session = Depends(get_db)
):
    """
    Update processing status.
    """

    try:

        status_obj = (

            ProcessingStatusService
            .get_status(

                doc_id,

                db

            )

        )

        return (

            ProcessingStatusService
            .update_status(

                status_obj,

                payload,

                db

            )

        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )


@router.delete(
    "/{doc_id}"
)
def delete_status(
    doc_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete processing status.
    """

    try:

        status_obj = (

            ProcessingStatusService
            .get_status(

                doc_id,

                db

            )

        )

        ProcessingStatusService.delete_status(

            status_obj,

            db

        )

        return {

            "message":

            "Deleted successfully"

        }

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )