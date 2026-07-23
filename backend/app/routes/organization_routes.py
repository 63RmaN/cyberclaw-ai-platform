from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal

from backend.app.services.organization_service import (
    get_organizations,
    create_organization
)

from backend.app.schemas.organization import (
    OrganizationResponse,
    OrganizationCreate
)


router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.get(
    "",
    response_model=list[OrganizationResponse]
)
def read_organizations(
    db: Session = Depends(get_db)
):
    return get_organizations(db)


@router.post(
    "",
    response_model=OrganizationResponse
)
def create_new_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):
    return create_organization(
        db,
        organization
    )