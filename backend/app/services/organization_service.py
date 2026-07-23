from sqlalchemy.orm import Session

from backend.app.models.organization import Organization
from backend.app.schemas.organization import OrganizationCreate


def get_organizations(db: Session):
    return db.query(Organization).all()


def create_organization(
    db: Session,
    organization: OrganizationCreate
):

    existing = (
        db.query(Organization)
        .filter(
            Organization.name == organization.name
        )
        .first()
    )

    if existing:
        return None


    db_organization = Organization(
        name=organization.name,
        description=organization.description
    )

    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)

    return db_organization