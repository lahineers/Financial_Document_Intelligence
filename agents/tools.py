from agno.tools import tool

from tools.comparison_tool import (
    ComparisonService
)


comparison_service = (
    ComparisonService()
)


@tool
def compare_metrics(

    old_metrics: dict,

    new_metrics: dict

):
    """
    Compare two financial metric sets.
    """

    return (

        comparison_service
        .compare_metrics(

            old_metrics,

            new_metrics

        )

    )