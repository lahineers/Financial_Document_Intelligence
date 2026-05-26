from services.metric_extraction_service import (
    MetricExtractionService
)

service = MetricExtractionService()

sample = """

Revenue: $120M

EBITDA: $22M

Net Profit: $18M

Total Assets: $450M

Total Liabilities: $120M

"""

print(
    service.extract_metrics(
        sample
    )
)