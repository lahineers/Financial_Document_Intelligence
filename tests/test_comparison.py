from services.comparison_service import (

    ComparisonService

)

service = ComparisonService()

old = {

    "Revenue":"120M",

    "Net Profit":"18M",

    "EBITDA":"22M"

}

new = {

    "Revenue":"150M",

    "Net Profit":"21M",

    "EBITDA":"25M"

}

print(

    service.compare_metrics(

        old,

        new

    )

)