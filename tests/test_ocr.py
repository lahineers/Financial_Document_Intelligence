from services.ocr_service import (

    OCRService

)

service = OCRService()

text = (

    service.extract_text(

        "sample.pdf"

    )

)

print(text)