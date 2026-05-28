from agents.orchestrator_agent import (
    orchestrator_agent
)


class AgentService:

    def process(

        self,

        query:str

    ):

        response = (

            orchestrator_agent.run(

                query

            )

        )

        return response.content


agent_service = (
    AgentService()
)