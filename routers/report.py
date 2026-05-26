from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.report import (
    ReportCreate,
    ReportUpdate,
    ReportResponse
)

from services.report_service import (
    ReportService
)


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.post(
    "/",
    response_model=ReportResponse
)
def create_report(
    payload: ReportCreate,
    db: Session = Depends(get_db)
):
    """
    Create report.
    """

    try:

        return ReportService.create_report(
            payload,
            db
        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            500,
            str(e)
        )


@router.get(
    "/",
    response_model=list[
        ReportResponse
    ]
)
def get_reports(
    db: Session = Depends(get_db)
):
    """
    Fetch reports.
    """

    try:

        return ReportService.get_reports(
            db
        )

    except Exception as e:

        raise HTTPException(
            500,
            str(e)
        )


@router.put(
    "/{report_id}",
    response_model=ReportResponse
)
def update_report(
    report_id: UUID,
    payload: ReportUpdate,
    db: Session = Depends(get_db)
):
    """
    Update report.
    """

    try:

        report = ReportService.get_report(
            report_id,
            db
        )

        return ReportService.update_report(
            report,
            payload,
            db
        )

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            500,
            str(e)
        )


@router.delete(
    "/{report_id}"
)
def delete_report(
    report_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete report.
    """

    try:

        report = ReportService.get_report(
            report_id,
            db
        )

        ReportService.delete_report(
            report,
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
            500,
            str(e)
        )