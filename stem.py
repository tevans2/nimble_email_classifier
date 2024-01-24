from nltk.stem import PorterStemmer

# Initialize the Porter Stemmer
porter_stemmer = PorterStemmer()

# Example word list
target_words = [
    "payment",
    "pay",
    "settle",
    "settlement",
    "agreement",
    "arrangement",
    "arrange",
    "balance",
    "due",
    "overdue",
    "outstanding",
    "arrears",
    "remit",
    "remittance",
    "clear",
    "resolve",
    "satisfy",
    "repay",
    "sum",
    "amount",
    "owed",
    "debt",
    "payment plan",
    "settlement offer",
    "payoff",
    "installment",
    "due date",
    "late",
    "collection",
    "outstanding balance",
    "negotiate",
    "reconciliation",
]

# Stem the words
stemmed_words = [porter_stemmer.stem(word) for word in target_words]

# Display the stemmed words
print(stemmed_words)

""" target_words = ['account numb', 'cannot open', 'open the stat', 'open the docu', 'open the fil', "can't open", 'not work', 'document', 'attach', 'password', 'unlock', 'encrypt', 'authent', 'secur', 'protect', 'detail', 'credenti', 'verif', 'passphras', 'key', 'troubleshoot', 'troubl', 'troubleshoot', 'trouble-shoot', 'open', 'access', 'unabl', 'detail', 'required detail', 'prompt', 'valid', 'assist', 'forgot', 'recal', 'resend', 'misplac', 'struggl', 'issu', 'help']"""
