from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
porter_stemmer = PorterStemmer()

# Example word list
target_words = [
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

# Stem the words
stemmed_words = [porter_stemmer.stem(word) for word in target_words]

# Display the stemmed words
print(stemmed_words)

""" target_words = ['account numb', 'cannot open', 'open the stat', 'open the docu', 'open the fil', "can't open", 'not work', 'document', 'attach', 'password', 'unlock', 'encrypt', 'authent', 'secur', 'protect', 'detail', 'credenti', 'verif', 'passphras', 'key', 'troubleshoot', 'troubl', 'troubleshoot', 'trouble-shoot', 'open', 'access', 'unabl', 'detail', 'required detail', 'prompt', 'valid', 'assist', 'forgot', 'recal', 'resend', 'misplac', 'struggl', 'issu', 'help']"""
