from datetime import datetime

from sqlalchemy.orm import Session

from backend.app.models.endpoint import Endpoint
from backend.app.models.organization import Organization

from backend.app.schemas.endpoint import EndpointCreate


def get_endpoints(
    db: Session
):

    return db.query(
        Endpoint
    ).all()



def create_endpoint(
    db: Session,
    endpoint: EndpointCreate
):

    organization = db.query(
        Organization
    ).filter(
        Organization.id == endpoint.organization_id
    ).first()


    if organization is None:

        return None


    new_endpoint = Endpoint(
        hostname=endpoint.hostname,
        operating_system=endpoint.operating_system,
        ip_address=endpoint.ip_address,
        agent_version=endpoint.agent_version,
        language=endpoint.language,
        organization_id=endpoint.organization_id
    )


    db.add(
        new_endpoint
    )

    db.commit()

    db.refresh(
        new_endpoint
    )


    return new_endpoint



def update_heartbeat(
    db: Session,
    endpoint_id: int
):

    endpoint = db.query(
        Endpoint
    ).filter(
        Endpoint.id == endpoint_id
    ).first()


    if endpoint is None:

        return None


    endpoint.last_heartbeat = datetime.utcnow()

    endpoint.status = "Online"


    db.commit()

    db.refresh(
        endpoint
    )


    return endpoint