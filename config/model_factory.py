from config.model_config import (
    MODEL_MAPPING
)

from agno.models.google import (
    Gemini
)

# later imports

# from agno.models.nvidia import Nvidia
# from agno.models.openai import OpenAIChat


def get_model(

    agent_name:str

):

    config = (

        MODEL_MAPPING[
            agent_name
        ]

    )

    provider = (

        config["provider"]

    )

    model_id = (

        config["id"]

    )

    if provider=="google":

        return Gemini(

            id=model_id

        )

    # NVIDIA later

    # if provider=="nvidia":
    #
    #     return Nvidia(
    #
    #         id=model_id
    #
    #     )

    raise ValueError(

        f"Unknown provider {provider}"

    )