from paddleocr import PaddleOCR
from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os


class OCRService:

    def __init__(self):

        self.ocr = PaddleOCR(

            use_angle_cls=True,

            lang="en"

        )

    def extract_text(

        self,

        pdf_path:str

    ):

        pages = convert_from_path(

            pdf_path

        )

        extracted = []

        for idx,page in enumerate(

            pages

        ):

            temp = (

                tempfile
                .NamedTemporaryFile(

                    suffix=".png",

                    delete=False

                )

            )

            page.save(

                temp.name,

                "PNG"

            )

            result = self.ocr.ocr(

                temp.name

            )

            page_text = []

            if result:

                for line in result[0]:

                    page_text.append(

                        line[1][0]

                    )

            extracted.append({

                "page":

                idx+1,

                "text":

                " ".join(

                    page_text

                )

            })

            os.remove(

                temp.name

            )

        return extracted