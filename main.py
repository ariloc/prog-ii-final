import sys

from python.src.files import *
from python.src.ngrams import *
from python.src.probability import *
from python.src.predictions import *
from python.src.solution import *

def main():
    if len(sys.argv) != 2:
        print("usage: python main.py [person_name]")
        exit(0)

    inputSentences = read_input_sentences(sys.argv[1])

    unigrams = extract_ngrams(inputSentences, 1)
    bigrams = extract_ngrams(inputSentences, 2)
    trigrams = extract_ngrams(inputSentences, 3)

    unigramProbability = compute_unigram_probability(unigrams)
    leftBigramProbability = compute_left_bigram_probability(bigrams)
    rightBigramProbability = compute_right_bigram_probability(bigrams)
    trigramProbability = compute_trigram_probability(trigrams)

    unigramPredicted = compute_unigram_predicted(unigramProbability)
    leftBigramPredicted = compute_left_bigram_predicted(unigramProbability, leftBigramProbability)
    rightBigramPredicted = compute_right_bigram_predicted(unigramProbability, rightBigramProbability)
    trigramPredicted = compute_trigram_predicted(unigramProbability, leftBigramProbability, rightBigramProbability, trigramProbability)

    dataset = (unigramPredicted, leftBigramPredicted, rightBigramPredicted, trigramPredicted)

    incompleteSentences = read_incomplete_sentences(sys.argv[1])
    completeSentences = solve_sentences(incompleteSentences, dataset)
    write_sentences(completeSentences, sys.argv[1])

if __name__ == "__main__":
    main()
