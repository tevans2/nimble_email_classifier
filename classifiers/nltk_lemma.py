# Purpose: Classify a phrase as asking or sharing intent using NLTK lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet

nltk.download("punkt")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")

lemmatizer = WordNetLemmatizer()


def lemmatize_words(word_list):
    lemmas = []
    for word, tag in nltk.pos_tag(word_list):
        wn_tag = get_wordnet_pos(tag)
        if wn_tag is not None:
            lemma = lemmatizer.lemmatize(word.lower(), pos=wn_tag)
        else:
            lemma = lemmatizer.lemmatize(word.lower())
        lemmas.append(lemma)
    return lemmas


def get_wordnet_pos(tag):
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return None


pwd_req_target_words = [
    "account number",
    "cannot open",
    "open the statement",
    "open the document",
    "open the file",
    "can't open",
    "not working",
    "document",
    "attachment",
    "password",
    "unlock",
    "encrypted",
    "authentication",
    "secured",
    "protected",
    "details",
    "credentials",
    "verification",
    "passphrase",
    "key",
    "troubleshooting",
    "trouble",
    "troubleshoot",
    "trouble-shooting",
    "opening",
    "access",
    "unable",
    "details",
    "required details",
    "prompt",
    "validate",
    "assist",
    "forgot",
    "recall",
    "resend",
    "misplaced",
    "struggling",
    "issues",
    "help",
]


def any_intersection(list1, list2):
    return any(word in list2 for word in list1)


def all_intersection(word_list, reference_list):
    return all(word in reference_list for word in word_list)


def classify_phrase_intent(text: str) -> str:
    lemmatized_words = lemmatize_words(word_tokenize(text))

    if any_intersection(pwd_req_target_words, lemmatized_words):
        return "1"
    return "0"
