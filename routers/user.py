from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from uuid import UUID

from db import get_db

from models.user import (
    User
)

from schemas.user import (
    UserCreate,
    UserUpdate,
    UserResponse
)

from passlib.context import (
    CryptContext
)


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def hash_password(
    password: str
):
    """
    Hash user password.
    """

    return pwd_context.hash(
        password
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

        existing_user = db.query(
            User
        ).filter(
            User.email
            ==
            payload.email
        ).first()

        if existing_user:

            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        existing_username = db.query(
            User
        ).filter(
            User.username
            ==
            payload.username
        ).first()

        if existing_username:

            raise HTTPException(
                status_code=400,
                detail="Username already exists"
            )

        user = User(

            username=payload.username,

            email=payload.email,

            hashed_password=
            hash_password(
                payload.password
            ),

            plan=payload.plan

        )

        db.add(
            user
        )

        db.commit()

        db.refresh(
            user
        )

        return user


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

        return db.query(
            User
        ).all()

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

    user = db.query(
        User
    ).filter(
        User.user_id
        ==
        user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


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

        user = db.query(
            User
        ).filter(
            User.user_id
            ==
            user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                user,
                key,
                value
            )

        db.commit()

        db.refresh(
            user
        )

        return user


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

        user = db.query(
            User
        ).filter(
            User.user_id
            ==
            user_id
        ).first()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        db.delete(
            user
        )

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
            status_code=500,
            detail=str(e)
        )