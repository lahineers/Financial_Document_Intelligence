from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import field_validator

from datetime import datetime
from uuid import UUID


ALLOWED_PLANS = {

    "free",

    "pro",

    "enterprise"

}


class UserCreate(BaseModel):
    """
    Schema for creating user.
    """

    username: str = Field(
        min_length=3,
        max_length=100
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=100
    )

    plan: str = "free"


    @field_validator(
        "plan"
    )
    @classmethod
    def validate_plan(
        cls,
        value
    ):

        if value not in ALLOWED_PLANS:

            raise ValueError(
                "Invalid plan"
            )

        return value


class UserUpdate(BaseModel):
    """
    Schema for updating user.
    """

    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    plan: str | None = None

    last_login: datetime | None = None


    @field_validator(
        "plan"
    )
    @classmethod
    def validate_plan(
        cls,
        value
    ):

        if value is None:

            return value

        if value not in ALLOWED_PLANS:

            raise ValueError(
                "Invalid plan"
            )

        return value


class UserResponse(BaseModel):
    """
    Returned user schema.
    """

    user_id: UUID

    username: str

    email: EmailStr

    plan: str

    created_at: datetime

    last_login: datetime | None


    class Config:

        from_attributes = True