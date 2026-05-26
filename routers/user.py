from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from services.user_service import (
    UserService
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Create user.
    """

    try:

        return UserService.create_user(
            payload,
            db
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
        UserResponse
    ]
)
def get_users(
    db: Session = Depends(get_db)
):
    """
    Fetch users.
    """

    try:

        return UserService.get_users(
            db
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Fetch user.
    """

    try:

        return UserService.get_user(
            user_id,
            db
        )

    except HTTPException:

        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_user(
    user_id: UUID,
    payload: UserUpdate,
    db: Session = Depends(get_db)
):
    """
    Update user.
    """

    try:

        user = UserService.get_user(
            user_id,
            db
        )

        return UserService.update_user(
            user,
            payload,
            db
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
    "/{user_id}"
)
def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db)
):
    """
    Delete user.
    """

    try:

        user = UserService.get_user(
            user_id,
            db
        )

        UserService.delete_user(
            user,
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