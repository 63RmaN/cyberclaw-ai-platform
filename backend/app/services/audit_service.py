from sqlalchemy.orm import Session

from backend.app.models.audit import AuditLog



def create_audit_log(
    db: Session,
    username: str,
    action: str,
    status: str,
    ip_address: str | None = None
):

    audit_entry = AuditLog(
        username=username,
        action=action,
        status=status,
        ip_address=ip_address
    )


    db.add(audit_entry)

    db.commit()

    db.refresh(audit_entry)


    return audit_entry



def get_audit_logs(
    db: Session
):

    return (
        db.query(AuditLog)
        .order_by(
            AuditLog.timestamp.desc()
        )
        .all()
    )