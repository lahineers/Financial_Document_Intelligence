from services.table_extraction_service import (

    TableExtractionService

)

service = (

    TableExtractionService()

)

tables = (

    service.extract_tables(

        "sample.pdf"

    )

)

print(tables)