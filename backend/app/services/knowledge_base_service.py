from sqlalchemy.orm import Session

from backend.app.models.knowledge_base import KnowledgeBase
from backend.app.schemas.knowledge_base import KnowledgeBaseCreate


def get_knowledge_bases(db: Session):

    return db.query(KnowledgeBase).all()



def create_knowledge_base(
    db: Session,
    knowledge_base: KnowledgeBaseCreate
):

    existing = (
        db.query(KnowledgeBase)
        .filter(
            KnowledgeBase.name == knowledge_base.name,
            KnowledgeBase.organization_id == knowledge_base.organization_id
        )
        .first()
    )


    if existing:
        return None



    db_knowledge_base = KnowledgeBase(
        name=knowledge_base.name,
        description=knowledge_base.description,
        type=knowledge_base.type,
        organization_id=knowledge_base.organization_id
    )


    db.add(db_knowledge_base)

    db.commit()

    db.refresh(db_knowledge_base)


    return db_knowledge_base