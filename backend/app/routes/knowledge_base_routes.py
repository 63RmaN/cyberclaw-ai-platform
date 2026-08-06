from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal
from backend.app.core.dependencies import get_current_user

from backend.app.services.knowledge_base_service import (
    get_knowledge_bases,
    create_knowledge_base
)

from backend.app.schemas.knowledge_base import (
    KnowledgeBaseCreate,
    KnowledgeBaseResponse
)


router = APIRouter(
    prefix="/knowledge-bases",
    tags=["Knowledge Bases"]
)



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.get(
    "",
    response_model=list[KnowledgeBaseResponse]
)
def read_knowledge_bases(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    return get_knowledge_bases(db)



@router.post(
    "",
    response_model=KnowledgeBaseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_knowledge_base(
    knowledge_base: KnowledgeBaseCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):

    result = create_knowledge_base(
        db,
        knowledge_base
    )


    if result is None:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Knowledge Base already exists"
        )


    return result