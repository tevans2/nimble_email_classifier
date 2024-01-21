# Main Script
from dotenv import load_dotenv
from preprocessing import preprocess_data
from evaluation import evaluate_classifier
import importlib
from tqdm import tqdm


def main():
    # Define the types of classifiers implemented in classifiers/ directory:
    load_dotenv()
    classifier_types = [
        "nltk_stemmer",
        "nltk_lemma",
        # "nltk_pos_tag",
        # "openai_davinci",
        # "openai_gpt35",
    ]

    # Load test phrases and their labels from csv file:
    data, labels = preprocess_data(
        "data/Nimble real data/pwd_req_real_data_formated.csv"
    )

    # Import the classifier modules dynamically based on the classifier types
    for classifier_type in classifier_types:
        classifier_module = importlib.import_module(f"classifiers.{classifier_type}")
        classifier_func = getattr(classifier_module, "classify_phrase_intent")

        predictions = [classifier_func(phrase) for phrase in tqdm(data)]
        evaluate_classifier(
            f"{classifier_type.capitalize()} Classifier", data, labels, predictions
        )


if __name__ == "__main__":
    main()
