from sqlalchemy.orm import Session

from fastapi import HTTPException

from models.user import (
    User
)

from models.saved_query import (
    SavedQuery
)

from schemas.saved_query import (
    SavedQueryCreate,
    SavedQueryUpdate
)


class SavedQueryService:
    """
    Handles saved query
    business logic.
    """


    @staticmethod
    def create_query(
        payload: SavedQueryCreate,
        db: Session
    ):
        """
        Create saved query.
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

        query = SavedQuery(

            **payload.model_dump()

        )

        db.add(
            query
        )

        db.commit()

        db.refresh(
            query
        )

        return query


    @staticmethod
    def get_queries(
        db: Session
    ):
        """
        Fetch queries.
        """

        return db.query(
            SavedQuery
        ).all()


    @staticmethod
    def get_query(
        query_id,
        db: Session
    ):
        """
        Fetch query.
        """

        query = db.query(
            SavedQuery
        ).filter(
            SavedQuery.query_id
            ==
            query_id
        ).first()

        if not query:

            raise HTTPException(
                404,
                "Saved query not found"
            )

        return query


    @staticmethod
    def update_query(
        query,
        payload,
        db: Session
    ):
        """
        Update query.
        """

        updates = payload.model_dump(
            exclude_unset=True
        )

        for key, value in updates.items():

            setattr(
                query,
                key,
                value
            )

        db.commit()

        db.refresh(
            query
        )

        return query


    @staticmethod
    def delete_query(
        query,
        db: Session
    ):
        """
        Delete query.
        """

        db.delete(
            query
        )

        db.commit()