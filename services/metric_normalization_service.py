from typing import Dict


class MetricNormalizationService:

    NORMALIZATION_MAP = {

        "Net Sales":
        "Revenue",

        "Total Revenue":
        "Revenue",

        "Sales Revenue":
        "Revenue",

        "Profit After Tax":
        "Net Profit",

        "Net Earnings":
        "Net Profit",

        "Cash From Operations":
        "Operating Cash Flow",

        "Operating Cash Generated":
        "Operating Cash Flow",

        "Assets":
        "Total Assets",

        "Liabilities":
        "Total Liabilities"

    }

    def normalize_metrics(
        self,
        metrics: Dict
    ) -> Dict:

        normalized = {}

        for key, value in metrics.items():

            canonical = (
                self.NORMALIZATION_MAP
                .get(key, key)
            )

            normalized[
                canonical
            ] = value

        return normalized