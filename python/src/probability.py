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
#  This probability @f$P(W^j)@f$ is calculated as the percentage each one @f$(W^j)@f$
#  represents from all the unigrams in a list of sentences.
#  @f[ P(W^j) = \frac{C(W^j)}{\sum_{k=1}^n C(W^k)} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences, and @f$C(x)@f$ is
#  the number of occurrences of the n-gram @f$x@f$ in the corpus.
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
#  This probability @f$P(W_i^j|W_{i-1})@f$ is calculated as the percentage each bigram
#  @f$(W_{i-1} W_i^j)@f$ (@f$j = 1,2,\dots,n@f$) represents from all bigrams <i>starting</i> 
#  in a certain word @f$W_{i-1}@f$:
#  @f[ P(W_i^j|W_{i-1}) = \frac{C(W_{i-1} W_i^j)}{\sum_{k=1}^n C(W_{i-1} W_i^k)} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences, and @f$C(x)@f$ is
#  the number of occurrences of the n-gram @f$x@f$ in the corpus.
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
#  This probability @f$P(W_i^j|W_{i+1})@f$ is calculated as the percentage each bigram
#  @f$(W_i^j W_{i+1})@f$ (@f$j = 1,2,\dots,n@f$) represents from all bigrams <i>ending</i> 
#  in a certain word @f$W_{i+1}@f$:
#  @f[ P(W_i^j|W_{i+1}) = \frac{C(W_i^j W_{i+1})}{\sum_{i=1}^n C(W_i^k W_{i+1})} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences, and @f$C(x)@f$ is
#  the number of occurrences of the n-gram @f$x@f$ in the corpus.
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
#  This probability @f$P(W_i^j|W_{i-1},W_{i+1})@f$ is calculated as the percentage each
#  trigram @f$(W_{i-1} W_i^j W_{i+1})@f$ (@f$j = 1,2,\dots,n@f$) represents from all trigrams 
#  <i>starting and ending</i> in a pair of words@f$W_{i-1}@f$ and @f$W_{i+1}@f$ respectively:
#  @f[ P(W_i^j|W_{i-1},W_{i+1}) = \frac{C(W_{i-1} W_i^j W_{i+1})}{\sum_{k=1}^n \#(W_{i-1} W_i^k W_{i+1})} @f]
#  where @f$n@f$ is the number of distinct words in the list of sentences, and @f$C(x)@f$ is
#  the number of occurrences of the n-gram @f$x@f$ in the corpus.
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
