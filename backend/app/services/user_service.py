from sqlalchemy.orm import Session

from backend.app.models.user import User
from backend.app.models.organization import Organization
from backend.app.schemas.user import UserCreate


def get_users(db: Session):

    return db.query(User).all()



def create_user(
    db: Session,
    user: UserCreate
):

    existing_user = (
        db.query(User)
        .filter(
            (User.username == user.username)
            |
            (User.email == user.email)
        )
        .first()
    )


    if existing_user:
        return None


    organization = (
        db.query(Organization)
        .filter(
            Organization.id == user.organization_id
        )
        .first()
    )


    if organization is None:
        return None


    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password,
        organization_id=user.organization_id
    )


    db.add(db_user)

    db.commit()

    db.refresh(db_user)


    return db_user