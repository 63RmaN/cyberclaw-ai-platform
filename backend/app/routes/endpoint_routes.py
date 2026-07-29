from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.permissions import require_admin

from backend.app.schemas.endpoint import (
    EndpointCreate,
    EndpointResponse
)

from backend.app.services.endpoint_service import (
    get_endpoints,
    create_endpoint,
    update_heartbeat
)


router = APIRouter(
    prefix="/endpoints",
    tags=["Endpoints"]
)


@router.get(
    "",
    response_model=list[EndpointResponse]
)
def read_endpoints(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):

    return get_endpoints(db)


@router.post(
    "",
    response_model=EndpointResponse,
    status_code=status.HTTP_201_CREATED
)
def register_endpoint(
    endpoint: EndpointCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):

    result = create_endpoint(
        db,
        endpoint
    )


    if result is None:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Organization does not exist"
        )


    return result


@router.post(
    "/{endpoint_id}/heartbeat",
    response_model=EndpointResponse
)
def heartbeat(
    endpoint_id: int,
    db: Session = Depends(get_db)
):

    result = update_heartbeat(
        db,
        endpoint_id
    )


    if result is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Endpoint not found"
        )


    return result