from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal

from backend.app.core.auth import decode_access_token

from backend.app.services.user_service import (
    get_user_by_username
)


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    username = decode_access_token(
        token
    )


    user = get_user_by_username(
        db,
        username
    )


    if user is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )


    return user