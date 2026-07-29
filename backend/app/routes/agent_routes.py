from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.database import SessionLocal

from backend.app.services.agent_service import (
    get_agents,
    create_agent
)

from backend.app.schemas.agent import (
    AgentResponse,
    AgentCreate
)


router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.get(
    "",
    response_model=list[AgentResponse]
)
def read_agents(
    db: Session = Depends(get_db)
):

    return get_agents(db)



@router.post(
    "",
    response_model=AgentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db)
):

    result = create_agent(
        db,
        agent
    )


    if result is None:

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Agent already exists or organization does not exist"
        )


    return result