# Purpose: Preprocess data from csv file
import csv

# from torch import LiteScriptModule


def preprocess_data(filename: str) -> tuple[list[str], list[str]]:
    phrases = []
    labels = []
    with open(filename, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=";")
        for row in csv_reader:
            phrase, label = row
            phrases.append(phrase)
            labels.append(label.strip())

    return phrases, labels
