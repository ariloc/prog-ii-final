## @file probability.py
#  @author Ariel Leonardo Fideleff

from .ngrams import Unigram, Bigram, Trigram

## Probability is represented as a @c float number between @c 0.0 and @c 1.0.
Probability = float

UnigramProbability = dict[Unigram, Probability]
BigramProbability = dict[Bigram, Probability]
TrigramProbability = dict[Trigram, Probability]
LeftBigramProbability = BigramProbability
RightBigramProbability = BigramProbability

## Computes the probability for each of the word unigrams in a list of sentences.
#
#  This probability @f$\text{P}(W_i)@f$ is calculated as the percentage each one @f$(W_i)@f$
#  represents from all the unigrams in a list of sentences.
#  @f[ \text{P}(W_i) = \frac{\#(W_i)}{\sum_{i=1}^n \#(W_i)} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences.
#
#  @param unigrams A dictionary with a count of each of the word unigrams occurring in a 
#                  list of sentences.
#  @return The probability calculated for each of the unigrams.
def compute_unigram_probability(unigrams: dict[Unigram, int]) -> UnigramProbability:
    totalUnigrams = 0
    for _, freq in unigrams.items():
        totalUnigrams += freq

    unigramProbability = {}
    for unigram, freq in unigrams.items():
        probability = freq / totalUnigrams
        unigramProbability[unigram] = probability

    return unigramProbability

## Computes the probability for each of the word left bigrams in a list of sentences.
#
#  This probability @f$\text{P}(W_j|W_i)@f$ is calculated as the percentage each bigram
#  @f$(W_i W_j)@f$ represents from all bigrams <i>starting</i> in a certain word @f$W_i@f$:
#  @f[ \text{P}(W_j|W_i) = \frac{\#(W_i W_j)}{\sum_{j=1}^n \#(W_i W_j)} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences.
#
#  @param bigrams A dictionary with the count of each of the word left bigrams occurring in a 
#                 list of sentences.
#  @return The probability calculated for each of the left bigrams.
def compute_left_bigram_probability(bigrams: dict[Bigram, int]) -> LeftBigramProbability:
    bigramPrefixes = {}
    for bigram, freq in bigrams.items():
        prefix = bigram[0]
        if not prefix in bigramPrefixes:
            bigramPrefixes[prefix] = 0
        bigramPrefixes[prefix] += freq

    leftBigramProbability = {}
    for bigram, freq in bigrams.items():
        prefix = bigram[0]
        probability = freq / bigramPrefixes[prefix]
        leftBigramProbability[bigram] = probability

    return leftBigramProbability

## Computes the probability for each of the word right bigrams in a list of sentences.
#
#  This probability @f$\text{P}(W_i|W_j)@f$ is calculated as the percentage each bigram
#  @f$(W_i W_j)@f$ represents from all bigrams <i>ending</i> in a certain word @f$W_j@f$:
#  @f[ \text{P}(W_i|W_j) = \frac{\#(W_i W_j)}{\sum_{i=1}^n \#(W_i W_j)} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences.
#
#  @param bigrams A dictionary with the count of each of the word right bigrams occurring in a 
#                 list of sentences.
#  @return The probability calculated for each of the right bigrams.
def compute_right_bigram_probability(bigrams: dict[Bigram, int]) -> RightBigramProbability:
    bigramSuffixes = {}
    for bigram, freq in bigrams.items():
        suffix = bigram[1]
        if not suffix in bigramSuffixes:
            bigramSuffixes[suffix] = 0
        bigramSuffixes[suffix] += freq

    rightBigramProbability = {}
    for bigram, freq in bigrams.items():
        suffix = bigram[1]
        probability = freq / bigramSuffixes[suffix]
        rightBigramProbability[bigram] = probability

    return rightBigramProbability

## Computes the probability for each of the word trigrams in a list of sentences.
#
#  This probability @f$\text{P}(W_j|W_i,W_k)@f$ is calculated as the percentage each trigram
#  @f$(W_i W_j W_k)@f$ represents from all trigrams <i>starting and ending</i> in a 
#  pair of words@f$W_i@f$ and @f$W_k@f$ respectively:
#  @f[ \text{P}(W_j|W_i,W_k) = \frac{\#(W_i W_j W_k)}{\sum_{j=1}^n \#(W_i W_j W_k)} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences.
#
#  @param trigrams A dictionary with the count of each of the word trigrams occurring in a 
#                  list of sentences.
#  @return The probability calculated for each of the trigrams.
def compute_trigram_probability(trigrams: dict[Trigram, int]) -> TrigramProbability:
    trigramEnds = {}
    for trigram, freq in trigrams.items():
        ends = (trigram[0],trigram[2])
        if not ends in trigramEnds:
            trigramEnds[ends] = 0
        trigramEnds[ends] += freq

    trigramProbability = {}
    for trigram, freq in trigrams.items():
        ends = (trigram[0],trigram[2])
        probability = freq / trigramEnds[ends]
        trigramProbability[trigram] = probability

    return trigramProbability
