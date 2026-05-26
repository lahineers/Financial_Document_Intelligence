from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.dashboard_metric import (
    DashboardMetric
)

from schemas.dashboard_metric import (
    DashboardMetricCreate,
    DashboardMetricUpdate
)


class DashboardMetricService:
    """
    Handles dashboard metric
    business logic.
    """


    @staticmethod
    def create_metric(
        payload: DashboardMetricCreate,
        db: Session
    ):
        """
        Create metric.
        """

        metric = DashboardMetric(

            **payload.model_dump()

        )

        db.add(
            metric
        )

        db.commit()

        db.refresh(
            metric
        )

        return metric


    @staticmethod
    def get_metrics(
        db: Session
    ):
        """
        Fetch metrics.
        """

        return db.query(
            DashboardMetric
        ).all()


    @staticmethod
    def get_metric(
        metric_id,
        db: Session
    ):
        """
        Fetch metric.
        """

        metric = db.query(
            DashboardMetric
        ).filter(
            DashboardMetric.metric_id
            ==
            metric_id
        ).first()

        if not metric:

            raise HTTPException(
                404,
                "Metric not found"
            )

        return metric


    @staticmethod
    def update_metric(
        metric,
        payload: DashboardMetricUpdate,
        db: Session
    ):
        """
        Update metric.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                metric,
                key,
                value
            )

        db.commit()

        db.refresh(
            metric
        )

        return metric


    @staticmethod
    def delete_metric(
        metric,
        db: Session
    ):
        """
        Delete metric.
        """

        db.delete(
            metric
        )

        db.commit()