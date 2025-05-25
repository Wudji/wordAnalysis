import re
import argparse
import numpy as np
import spacy
from nltk.corpus import stopwords

try:
    stop = set(stopwords.words('english'))
except LookupError:
    import nltk
    nltk.download('stopwords')
    stop = set(stopwords.words('english'))

nlp = spacy.load('en_core_web_lg')
stopwords_combined = set(stopwords.words('english')).union(nlp.Defaults.stop_words)


def preprocess(text):
    cleaned = re.sub(r"[^A-Za-z\\. ]+", " ", text).lower()
    doc = nlp(cleaned)

    stop_combined = set(stopwords.words('english')).union(nlp.Defaults.stop_words)

    tokens = [tok.text for tok in doc if tok.is_alpha and tok.text not in stop_combined and len(tok.text) > 2]
    sents = [sent.text.strip() for sent in doc.sents]
    return tokens, sents

def compute_syntax_stats(text):
    """
    Compute average sentence length and mean dependency distance.
    """
    doc = nlp(text)
    sent_lengths = [len(sent) for sent in doc.sents]
    deps = [tok.head.i - tok.i for tok in doc if tok.dep_ != 'ROOT']
    return np.mean(sent_lengths), np.mean(np.abs(deps))

def main(args):
    # Read inputs
    with open(args.magazine, 'r', encoding='utf-8') as f:
        mag_text = f.read()
    with open(args.paper, 'r', encoding='utf-8') as f:
        pap_text = f.read()

    # Preprocess
    mag_tokens, mag_sents = preprocess(mag_text)
    pap_tokens, pap_sents = preprocess(pap_text)

    # Syntax stats
    mag_sent_len, mag_dep = compute_syntax_stats(mag_text)
    pap_sent_len, pap_dep = compute_syntax_stats(pap_text)

    print("=== Syntax Complexity ===")
    print(f"Magazine Avg. Sentence Length: {mag_sent_len:.2f} words")
    print(f"Paper Avg. Sentence Length:    {pap_sent_len:.2f} words")
    print(f"Magazine Avg. Dependency Distance: {mag_dep:.2f}")
    print(f"Paper Avg. Dependency Distance:    {pap_dep:.2f}\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compare magazine vs paper texts')
    parser.add_argument('--magazine', required=True, help='Path to magazine text file')
    parser.add_argument('--paper',    required=True, help='Path to paper text file')
    args = parser.parse_args()
    main(args)
