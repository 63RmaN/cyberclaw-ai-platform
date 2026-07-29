from sqlalchemy.orm import Session

from backend.app.core.security import get_password_hash

from backend.app.models.user import User
from backend.app.models.organization import Organization
from backend.app.schemas.user import UserCreate



def get_users(db: Session):

    return db.query(User).all()



def create_user(
    db: Session,
    user: UserCreate
):

    if user.role not in ["admin", "user"]:

        return None


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

        hashed_password=get_password_hash(
            user.password
        ),

        organization_id=user.organization_id,

        role=user.role
    )



    db.add(db_user)

    db.commit()

    db.refresh(db_user)


    return db_user




def get_user_by_username(
    db: Session,
    username: str
):

    return (

        db.query(User)

        .filter(
            User.username == username
        )

        .first()

    )