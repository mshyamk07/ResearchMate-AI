import re


class MetadataService:

    @staticmethod
    def extract(text: str):

        metadata = {
            "doi": "Unknown",
            "publication_date": "Unknown",
            "abstract": "Unknown"
        }

        # DOI
        doi_match = re.search(
            r"10\.\d{4,9}/[-._;()/:A-Z0-9]+",
            text,
            re.IGNORECASE
        )

        if doi_match:
            metadata["doi"] = doi_match.group(0)

        # Publication date
        date_match = re.search(
            r"date of publication\s+(.+?)\.",
            text,
            re.IGNORECASE
        )

        if date_match:
            metadata["publication_date"] = date_match.group(1).strip()

        # Abstract
        abstract_match = re.search(
            r"Abstract(.*?)(?=\n[A-Z ]{3,}|Index Terms|Keywords)",
            text,
            re.DOTALL | re.IGNORECASE
        )

        if abstract_match:
            metadata["abstract"] = " ".join(
                abstract_match.group(1).split()
            )

        return metadata