from services.document_classifier_service import (

    DocumentClassifierService

)

service = (

    DocumentClassifierService()

)

sample = """

Quarterly Report

Three Months Ended

Revenue 150M

Net Profit 21M

"""

print(

    service.classify(

        sample

    )

)