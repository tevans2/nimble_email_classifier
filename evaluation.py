# Purpose: Contains functions for evaluating the performance of classifiers.
from sklearn.metrics import classification_report
from datetime import datetime


def evaluate_classifier(
    classifier_name: str,
    phrases: list[str],
    labels: list[str],
    predictions: list[str],
    output_file: str = "Perfromance log/performance_log.txt",  # Default output file
) -> None:
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the file in append mode
    with open(output_file, "a") as file:
        file.write(f"\n{current_datetime} - {classifier_name} Performance:\n")
        file.write(classification_report(labels, predictions, zero_division=1))

        incorrect_predictions = [
            f"Phrase: '{phrases[i]}', Predicted: '{predictions[i]}', Actual: '{labels[i]}'"
            for i in range(len(labels))
            if labels[i] != predictions[i]
        ]

    #        file.write("\nIncorrectly classified phrases:\n")
    #        for incorrect in incorrect_predictions:
    #            file.write(incorrect + "\n")

    # Print the results to the console
    print(f"\n{current_datetime} - {classifier_name} Performance:\n")
    print(classification_report(labels, predictions, zero_division=1))

    print("\nIncorrectly classified phrases:")
    for incorrect in incorrect_predictions:
        print(incorrect)
