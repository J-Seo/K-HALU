import datasets
import re


def process_docs(dataset: datasets.Dataset) -> datasets.Dataset:
    def _process_doc(doc):
        knowledge = "작성일: " + doc["date"].strip() + '\n' + "문서: " + doc["document"].strip()
        instruction = doc["instruction"].strip()

        out_doc = {
            "query": knowledge + '\n' + instruction + '\n',
            "choices": [f"{i}. {doc[str(i)]}" for i in range(1,6)],
            "gold": doc["label"],
        }
        return out_doc

    return dataset.map(_process_doc)
