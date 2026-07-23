from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal
from backend.app.services.organization_service import get_organizations
from backend.app.schemas.organization import OrganizationResponse


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