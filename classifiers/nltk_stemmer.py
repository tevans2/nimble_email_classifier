# Purpose: NLTK Stemmer
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
nltk.download("punkt")  # download the necessary package

stemmer = PorterStemmer()

pwd_req_stems = [
    "account numb",
    "cannot open",
    "can't open",
    "not work",
    "document",
    "attach",
    "password",
    "unlock",
    "encrypt",
    "authent",
    "secur",
    "protect",
    "detail",
    "credenti",
    "verif",
    "passphras",
    "key",
    "troubleshoot",
    "troubl",
    "troubleshoot",
    "trouble-shoot",
    "open",
    "access",
    "unabl",
    "detail",
    "required",
    "prompt",
    "valid",
    "assist",
    "forgot",
    "recal",
    "resend",
    "misplac",
    "struggl",
    "issu",
    "help",
]


def any_intersection(list1, list2):
    return any(word in list2 for word in list1)


def all_intersection(word_list, reference_list):
    return all(word in reference_list for word in word_list)


def classify_phrase_intent(text: str) -> str:
    stemmed_words = [stemmer.stem(w) for w in word_tokenize(text)]

    if any_intersection(pwd_req_stems, stemmed_words):
        return "1"
    return "0"
