from .ngrams import Unigram, Bigram, Trigram

UnigramProbability = dict[Unigram, float]
BigramProbability = dict[Bigram, float]
TrigramProbability = dict[Trigram, float]
LeftBigramProbability = BigramProbability
RightBigramProbability = BigramProbability

def compute_unigram_probability(unigrams: dict[Unigram, int]) -> UnigramProbability:
    totalUnigrams = 0
    for _, freq in unigrams.items():
        totalUnigrams += freq

    unigramProbability = {}
    for unigram, freq in unigrams.items():
        probability = freq / totalUnigrams
        unigramProbability[unigram] = probability

    return unigramProbability

# TODO: Combine bigrams?
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
