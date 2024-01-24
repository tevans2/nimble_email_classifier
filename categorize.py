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
        "C:/Users/TateE/Documents/data/Nimble real data/payment_binary_small_sample.csv"
    )

    # Import the classifier modules dynamically based on the classifier types
    for classifier_type in classifier_types:
        classifier_module = importlib.import_module(f"classifiers.{classifier_type}")
        classifier_func = getattr(classifier_module, "classify_phrase_intent")

        predictions = [classifier_func(phrase) for phrase in tqdm(data)]
        evaluate_classifier(
            f"{classifier_type.capitalize()} Classifier", data, labels, predictions
        )


def categorize(phrase: str):
    # Define the types of classifiers implemented in classifiers/ directory:
    load_dotenv()
    classifier_types = [
        "nltk_stemmer",
        "nltk_lemma",
        # "nltk_pos_tag",
        # "openai_davinci",
        "openai_gpt35",
    ]

    predictions = []
    # Import the classifier modules dynamically based on the classifier types
    for classifier_type in classifier_types:
        classifier_module = importlib.import_module(f"classifiers.{classifier_type}")
        classifier_func = getattr(classifier_module, "classify_phrase_intent")

        prediction = [classifier_func(phrase)]

        predictions.append(int(prediction[0]))

    final_prediction = majority_vote(predictions)

    return final_prediction


def majority_vote(predictions):
    count_ones = predictions[0] + predictions[1] + predictions[2]
    count_zeros = 3 - count_ones

    if count_ones > count_zeros:
        return 1
    elif count_zeros > count_ones:
        return 0
    else:
        return None


if __name__ == "__main__":
    main()
