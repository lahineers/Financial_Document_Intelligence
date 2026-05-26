import camelot


class TableExtractionService:

    def extract_tables(

        self,

        pdf_path: str

    ):

        tables = camelot.read_pdf(

            pdf_path,

            pages="all",

            flavor="lattice"

        )

        extracted = []

        for idx, table in enumerate(

            tables

        ):

            extracted.append({

                "table_id":

                idx + 1,

                "rows":

                table.df.to_dict(

                    orient="records"

                )

            })

        return extracted