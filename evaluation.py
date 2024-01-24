# Purpose: Contains functions for evaluating the performance of classifiers.
from sklearn.metrics import classification_report
from datetime import datetime


def evaluate_classifier(
    classifier_name: str,
    phrases: list[str],
    labels: list[str],
    predictions: list[str],
    output_file: str = "C:/Users/TateE/Documents/nimble_email_classifier/Performance log/performance_log.txt",  # Default output file
) -> None:
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Open the file in append mode
    with open(output_file, "w") as file:
        file.write(f"\n{current_datetime} - {classifier_name} Performance:\n")
        file.write(classification_report(labels, predictions, zero_division=1))

        correct_predictions = [
            f"Phrase: '{phrases[i]}', Predicted: '{predictions[i]}', Actual: '{labels[i]}'"
            for i in range(len(labels))
            if predictions[i] == "1"
        ]

        incorrect_predictions = [
            f"Phrase: '{phrases[i]}', Predicted: '{predictions[i]}', Actual: '{labels[i]}'"
            for i in range(len(labels))
            if labels[i] != predictions[i]
        ]

        file.write("\nCorrectly classified phrases:\n")
        for correct in correct_predictions:
            file.write(correct + "\n")

    # Print the results to the console
    print(f"\n{current_datetime} - {classifier_name} Performance:\n")
    print(classification_report(labels, predictions, zero_division=1))


"""
    print("\nIncorrectly classified phrases:")
    for incorrect in incorrect_predictions:
        print(incorrect)
"""
