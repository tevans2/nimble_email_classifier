# Purpose: Hugging Face Zero-Shot Classification Pipeline
from transformers.pipelines import pipeline

# Hugging Face Zero-Shot Classification Pipeline uses latest version of facebook/bart-large-mnli
# Multi-Genre Natural Language Inference (MNLI) with BART
classifier = pipeline("zero-shot-classification")

categories = [
    "asking for permission",
    "share",
    "storing, stored, recorded, included, reviewing, written, registering, documented, considered, noting, talking, meeting",
]

category_mapping = {
    categories[0]: "ask",
    categories[1]: "shared",
    categories[2]: "unclear",
}


def classify_phrase_intent(text: str) -> str:
    result = classifier(text, categories)
    # classified returns:
    # A `dict` or a list of `dict`: Each result comes as a dictionary with the following keys:
    # - **sequence** (`str`) -- The sequence for which this is the output.
    # - **labels** (`List[str]`) -- The labels sorted by order of likelihood.
    # - **scores** (`List[float]`) -- The probabilities for each of the labels.
    # return the class with the highest score

    result_category = str(result["labels"][0])  # type: ignore

    mapped_category = category_mapping.get(result_category, "unclear")

    return mapped_category
