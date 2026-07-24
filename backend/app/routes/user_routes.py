from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal

from backend.app.services.user_service import (
    get_users,
    create_user
)

from backend.app.schemas.user import (
    UserResponse,
    UserCreate
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.get(
    "",
    response_model=list[UserResponse]
)
def read_users(
    db: Session = Depends(get_db)
):

    return get_users(db)



@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    result = create_user(
        db,
        user
    )


    if result is None:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists or organization does not exist"
        )


    return result