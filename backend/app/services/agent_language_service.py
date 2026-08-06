from sqlalchemy.orm import Session

from backend.app.models.agent import Agent
from backend.app.models.agent_language import AgentLanguage

from backend.app.schemas.agent_language import AgentLanguageCreate


def get_agent_languages(
    db: Session,
    agent_id: int
):

    return (
        db.query(AgentLanguage)
        .filter(
            AgentLanguage.agent_id == agent_id
        )
        .all()
    )


def add_agent_language(
    db: Session,
    agent_id: int,
    language: AgentLanguageCreate
):

    agent = (
        db.query(Agent)
        .filter(
            Agent.id == agent_id
        )
        .first()
    )

    if agent is None:
        return None


    existing = (
        db.query(AgentLanguage)
        .filter(
            AgentLanguage.agent_id == agent_id,
            AgentLanguage.language == language.language
        )
        .first()
    )

    if existing:
        return "exists"


    if language.is_default:

        (
            db.query(AgentLanguage)
            .filter(
                AgentLanguage.agent_id == agent_id
            )
            .update(
                {
                    AgentLanguage.is_default: False
                }
            )
        )


    new_language = AgentLanguage(
        agent_id=agent_id,
        language=language.language,
        is_default=language.is_default
    )

    db.add(new_language)

    db.commit()

    db.refresh(new_language)

    return new_language