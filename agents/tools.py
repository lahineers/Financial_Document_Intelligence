from agno.tools import tool

from services.comparison_service import (
    ComparisonService
)

from services.table_extraction_service import (
    TableExtractionService
)


comparison_service = (
    ComparisonService()
)

table_service = (
    TableExtractionService()
)


@tool
def extract_tables(
    pdf_path: str
):
    """
    Extract tables from financial PDF.
    """

    return (

        table_service
        .extract_tables(pdf_path)

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