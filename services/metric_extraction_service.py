import re
from typing import Dict, Optional


class MetricExtractionService:

    METRIC_PATTERNS = {

        "Revenue": [

            r"Revenue\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)",

            r"Net Sales\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)",

            r"Total Revenue\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)"

        ],

        "Net Profit": [

            r"Net Profit\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)",

            r"Profit After Tax\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)",

            r"Net Earnings\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)"

        ],

        "EBITDA": [

            r"EBITDA\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)"

        ],

        "Operating Cash Flow": [

            r"Operating Cash Flow\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)",

            r"Cash From Operations\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)"

        ],

        "Total Assets": [

            r"Total Assets\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)"

        ],

        "Total Liabilities": [

            r"Total Liabilities\s*[:\-]?\s*\$?([\d,.]+(?:\.\d+)?\s*[MBK]?)"

        ]

    }

    def extract_metrics(
        self,
        text: str
    ) -> Dict[str, Optional[str]]:

        extracted = {}

        for metric, patterns in self.METRIC_PATTERNS.items():

            extracted[metric] = None

            for pattern in patterns:

                match = re.search(
                    pattern,
                    text,
                    re.IGNORECASE
                )

                if match:

                    extracted[metric] = (
                        match.group(1)
                    )

                    break

        return extracted