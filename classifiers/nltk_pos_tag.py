# Purpose: NLTK Part Of Speech (POS) Tagger
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser

nltk.download("averaged_perceptron_tagger")


def classify_phrase_intent(text: str) -> str:
    grammar = r"""
        PERMISSION: {<MD><PRP|VB|VBP><.*>*<VB|VBP>}
        NOTIFICATION: {<.*><VBD><.*>*<NN|NNS|NNP|NNPS>}
    """

    parser = RegexpParser(grammar)

    # Tokenize and tag the words in the phrase
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)

    # Chunk the tagged tokens based on the defined grammar
    tree = parser.parse(tagged_tokens)

    # Extract the chunks and their labels
    chunks = nltk.chunk.tree2conlltags(tree)
    labels = [label for _, _, label in chunks]

    # Determine the overall intent based on the extracted labels
    if "PERMISSION" in labels:
        return "ask"
    elif "NOTIFICATION" in labels:
        return "shared"
    else:
        return "unclear"
