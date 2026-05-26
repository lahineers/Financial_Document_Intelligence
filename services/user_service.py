from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.user import User

from schemas.user import (
    UserCreate,
    UserUpdate
)

from passlib.context import (
    CryptContext
)


pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)


class UserService:
    """
    Handles user business logic.
    """

    @staticmethod
    def hash_password(
        password: str
    ):
        """
        Hash password.
        """

        return pwd_context.hash(
            password
        )


    @staticmethod
    def create_user(
        payload: UserCreate,
        db: Session
    ):
        """
        Create user.
        """

        existing_email = db.query(
            User
        ).filter(
            User.email
            ==
            payload.email
        ).first()

        if existing_email:

            raise HTTPException(
                400,
                "Email already exists"
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
                400,
                "Username already exists"
            )

        user = User(

            username=
            payload.username,

            email=
            payload.email,

            hashed_password=
            UserService.hash_password(
                payload.password
            ),

            plan=
            payload.plan

        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user


    @staticmethod
    def get_users(
        db: Session
    ):
        """
        Fetch users.
        """

        return db.query(
            User
        ).all()


    @staticmethod
    def get_user(
        user_id,
        db: Session
    ):
        """
        Fetch single user.
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
                404,
                "User not found"
            )

        return user


    @staticmethod
    def update_user(
        user,
        payload: UserUpdate,
        db: Session
    ):
        """
        Update user.
        """

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

        db.refresh(user)

        return user


    @staticmethod
    def delete_user(
        user,
        db: Session
    ):
        """
        Delete user.
        """

        db.delete(user)

        db.commit()