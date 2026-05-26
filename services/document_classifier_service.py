import re


class DocumentClassifierService:

    DOCUMENT_PATTERNS = {

        "Annual Report":[

            r"annual report",

            r"shareholders",

            r"fiscal year"

        ],

        "Quarterly Report":[

            r"quarter ended",

            r"quarterly report",

            r"three months ended"

        ],

        "Balance Sheet":[

            r"balance sheet",

            r"assets",

            r"liabilities"

        ],

        "Income Statement":[

            r"income statement",

            r"revenue",

            r"net profit"

        ],

        "Cash Flow Statement":[

            r"cash flow statement",

            r"operating activities",

            r"financing activities"

        ],

        "Audit Report":[

            r"independent auditor",

            r"audit opinion",

            r"auditor report"

        ]

    }

    def classify(

        self,

        text:str

    ):

        text = text.lower()

        scores = {}

        for doc_type,patterns in (

            self.DOCUMENT_PATTERNS
            .items()

        ):

            score = 0

            for pattern in patterns:

                if re.search(

                    pattern,

                    text

                ):

                    score += 1

            scores[doc_type] = score

        best = max(

            scores,

            key=scores.get

        )

        if scores[best] == 0:

            return "Unknown"

        return best