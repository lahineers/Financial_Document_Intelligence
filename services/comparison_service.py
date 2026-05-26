from typing import Dict


class ComparisonService:

    COMPARABLE_METRICS = [

        "Revenue",

        "Net Profit",

        "EBITDA",

        "Operating Cash Flow",

        "Total Assets",

        "Total Liabilities"

    ]

    def compare_metrics(

        self,

        old_metrics: Dict,

        new_metrics: Dict

    ) -> Dict:

        comparison = {}

        for metric in self.COMPARABLE_METRICS:

            old = old_metrics.get(metric)

            new = new_metrics.get(metric)

            if not old or not new:

                continue

            try:

                old_num = self._parse_number(old)

                new_num = self._parse_number(new)

                diff = new_num - old_num

                pct = (

                    diff / old_num * 100

                    if old_num != 0

                    else None

                )

                comparison[metric] = {

                    "old": old,

                    "new": new,

                    "difference":

                    round(diff,2),

                    "percentage_change":

                    (

                        round(pct,2)

                        if pct is not None

                        else None

                    )

                }

            except:

                continue

        return comparison

    def _parse_number(

        self,

        value: str

    ):

        value = value.upper()

        multiplier = 1

        if value.endswith("M"):

            multiplier = 1_000_000

            value = value[:-1]

        elif value.endswith("K"):

            multiplier = 1_000

            value = value[:-1]

        elif value.endswith("B"):

            multiplier = 1_000_000_000

            value = value[:-1]

        return (

            float(

                value.replace(",","")

            )

            * multiplier

        )