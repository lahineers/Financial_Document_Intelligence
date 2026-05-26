from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.dashboard_metric import (
    DashboardMetric
)

from schemas.dashboard_metric import (
    DashboardMetricCreate,
    DashboardMetricUpdate,
    DashboardMetricResponse
)


router = APIRouter(
    prefix="/dashboard-metrics",
    tags=["Dashboard Metrics"]
)


@router.post(
    "/",
    response_model=DashboardMetricResponse
)
def create_metric(
    payload: DashboardMetricCreate,
    db: Session = Depends(get_db)
):
    """
    Create dashboard metric.
    """

    try:

        exists = db.query(
            DashboardMetric
        ).filter(
            DashboardMetric.metric_name
            ==
            payload.metric_name
        ).first()

        if exists:

            raise HTTPException(
                400,
                "Metric already exists"
            )

        metric = DashboardMetric(
            metric_name=payload.metric_name,
            metric_value=payload.metric_value,
            metric_category=payload.metric_category
        )

        db.add(metric)

        db.commit()

        db.refresh(metric)

        return metric

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
        DashboardMetricResponse
    ]
)
def get_metrics(
    db: Session = Depends(get_db)
):
    """
    Fetch metrics.
    """

    try:

        return db.query(
            DashboardMetric
        ).all()

    except Exception as e:

        raise HTTPException(
            500,
            str(e)
        )


@router.put(
    "/{metric_id}",
    response_model=DashboardMetricResponse
)
def update_metric(
    metric_id: UUID,
    payload: DashboardMetricUpdate,
    db: Session = Depends(get_db)
):
    """
    Update metric.
    """

    try:

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

        db.refresh(metric)

        return metric

    except HTTPException:

        raise

    except Exception as e:

        db.rollback()

        raise HTTPException(
            500,
            str(e)
        )


@router.delete(
    "/{metric_id}"
)
def delete_metric(
    metric_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete metric.
    """

    try:

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

        db.delete(metric)

        db.commit()

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