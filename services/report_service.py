from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.user import User

from models.upload_session import (
    UploadSession
)

from models.report import (
    Report
)

from schemas.report import (
    ReportCreate,
    ReportUpdate
)


class ReportService:
    """
    Handles report
    business logic.
    """


    @staticmethod
    def create_report(
        payload: ReportCreate,
        db: Session
    ):
        """
        Create report.
        """

        user = db.query(
            User
        ).filter(
            User.user_id
            ==
            payload.user_id
        ).first()

        if not user:

            raise HTTPException(
                404,
                "User not found"
            )

        session = db.query(
            UploadSession
        ).filter(
            UploadSession.session_id
            ==
            payload.session_id
        ).first()

        if not session:

            raise HTTPException(
                404,
                "Session not found"
            )

        report = Report(

            **payload.model_dump()

        )

        db.add(
            report
        )

        db.commit()

        db.refresh(
            report
        )

        return report


    @staticmethod
    def get_reports(
        db: Session
    ):
        """
        Fetch reports.
        """

        return db.query(
            Report
        ).all()


    @staticmethod
    def get_report(
        report_id,
        db: Session
    ):
        """
        Fetch report.
        """

        report = db.query(
            Report
        ).filter(
            Report.report_id
            ==
            report_id
        ).first()

        if not report:

            raise HTTPException(
                404,
                "Report not found"
            )

        return report


    @staticmethod
    def update_report(
        report,
        payload: ReportUpdate,
        db: Session
    ):
        """
        Update report.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                report,
                key,
                value
            )

        db.commit()

        db.refresh(
            report
        )

        return report


    @staticmethod
    def delete_report(
        report,
        db: Session
    ):
        """
        Delete report.
        """

        db.delete(
            report
        )

        db.commit()