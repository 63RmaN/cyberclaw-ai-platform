from fastapi import Depends, HTTPException, status

from backend.app.core.dependencies import get_current_user


def require_admin(
    current_user = Depends(get_current_user)
):

    if current_user.role != "admin":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )


    return current_user