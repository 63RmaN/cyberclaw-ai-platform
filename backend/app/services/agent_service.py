from sqlalchemy.orm import Session

from backend.app.models.agent import Agent
from backend.app.models.organization import Organization

from backend.app.schemas.agent import AgentCreate



def get_agents(
    db: Session
):

    return db.query(
        Agent
    ).all()



def create_agent(
    db: Session,
    agent: AgentCreate
):

    organization = (
        db.query(Organization)
        .filter(
            Organization.id == agent.organization_id
        )
        .first()
    )


    if organization is None:
        return None



    existing = (
        db.query(Agent)
        .filter(
            Agent.name == agent.name,
            Agent.organization_id == agent.organization_id
        )
        .first()
    )


    if existing:
        return None



    db_agent = Agent(
        name=agent.name,
        description=agent.description,
        language=agent.language,
        industry=agent.industry,
        role=agent.role,
        organization_id=agent.organization_id
    )


    db.add(
        db_agent
    )

    db.commit()

    db.refresh(
        db_agent
    )


    return db_agent