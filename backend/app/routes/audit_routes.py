from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.core.dependencies import get_db
from backend.app.core.permissions import require_admin

from backend.app.services.audit_service import (
    get_audit_logs
)

from backend.app.models.audit import AuditLog


router = APIRouter(
    prefix="/audit",
    tags=["Audit"]
)



@router.get(
    "",
    response_model=list[dict]
)
def read_audit_logs(
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):

    logs = get_audit_logs(db)


    return [
        {
            "id": log.id,
            "username": log.username,
            "action": log.action,
            "status": log.status,
            "ip_address": log.ip_address,
            "timestamp": log.timestamp
        }
        for log in logs
    ]