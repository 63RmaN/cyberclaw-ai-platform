from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.permissions import require_admin

from backend.app.services.user_service import (
    get_users,
    create_user
)

from backend.app.services.audit_service import (
    create_audit_log
)

from backend.app.schemas.user import (
    UserResponse,
    UserCreate
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)



@router.get(
    "",
    response_model=list[UserResponse]
)
def read_users(
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):

    return get_users(db)



@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_user(
    request: Request,
    user: UserCreate,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):

    client_ip = request.client.host if request.client else None


    result = create_user(
        db,
        user
    )


    if result is None:

        create_audit_log(
            db,
            username=current_user.username,
            action="CREATE_USER",
            status="FAILED",
            ip_address=client_ip
        )


        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists or organization does not exist"
        )



    create_audit_log(
        db,
        username=current_user.username,
        action="CREATE_USER",
        status="SUCCESS",
        ip_address=client_ip
    )


    return result