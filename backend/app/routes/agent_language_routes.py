from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.permissions import require_admin

from backend.app.schemas.agent_language import (
    AgentLanguageCreate,
    AgentLanguageResponse
)

from backend.app.services.agent_language_service import (
    add_agent_language,
    get_agent_languages
)


router = APIRouter(
    prefix="/agents/{agent_id}/languages",
    tags=["Agent Languages"]
)


@router.get(
    "",
    response_model=list[AgentLanguageResponse]
)
def read_agent_languages(
    agent_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):

    return get_agent_languages(
        db,
        agent_id
    )


@router.post(
    "",
    response_model=AgentLanguageResponse,
    status_code=status.HTTP_201_CREATED
)
def create_agent_language(
    agent_id: int,
    language: AgentLanguageCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):

    result = add_agent_language(
        db,
        agent_id,
        language
    )


    if result is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Agent not found"
        )


    if result == "exists":

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Language already exists"
        )


    return result