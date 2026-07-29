from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal

from backend.app.services.user_service import (
    get_user_by_username
)

from backend.app.services.audit_service import (
    create_audit_log
)

from backend.app.core.security import (
    verify_password
)

from backend.app.core.token import (
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.post("/login")
def login(
    request: Request,
    username: str,
    password: str,
    db: Session = Depends(get_db)
):

    client_ip = request.client.host if request.client else None


    user = get_user_by_username(
        db,
        username
    )


    if user is None:

        create_audit_log(
            db,
            username=username,
            action="LOGIN",
            status="FAILED",
            ip_address=client_ip
        )


        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )



    if not verify_password(
        password,
        user.hashed_password
    ):


        create_audit_log(
            db,
            username=username,
            action="LOGIN",
            status="FAILED",
            ip_address=client_ip
        )


        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )



    if not user.is_active:


        create_audit_log(
            db,
            username=username,
            action="LOGIN",
            status="BLOCKED",
            ip_address=client_ip
        )


        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is disabled"
        )



    create_audit_log(
        db,
        username=user.username,
        action="LOGIN",
        status="SUCCESS",
        ip_address=client_ip
    )



    access_token = create_access_token(
        {
            "sub": user.username
        }
    )


    return {
        "access_token": access_token,
        "token_type": "bearer"
    }