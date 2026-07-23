from sqlalchemy.orm import Session

from backend.app.models.organization import Organization


def get_organizations(db: Session):
    return db.query(Organization).all()