from fastapi import APIRouter

from schemas.agent_schema import (

    AgentRequest,

    AgentResponse

)

from services.agent_service import (

    agent_service

)


router = APIRouter(

    prefix="/agent",

    tags=["Agent"]

)


@router.post(

    "/query",

    response_model=AgentResponse

)

def process_query(

    request:AgentRequest

):

    result = (

        agent_service.process(

            request.query

        )

    )

    return AgentResponse(

        response=result

    )