from services.metric_normalization_service import (
    MetricNormalizationService
)

service = (
    MetricNormalizationService()
)

sample = {

    "Net Sales":"120M",

    "Profit After Tax":
    "18M",

    "Assets":"450M"

}

print(

    service.normalize_metrics(
        sample
    )

)