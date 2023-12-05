from .probability import UnigramProbability, LeftBigramProbability, RightBigramProbability, TrigramProbability

Word = str
Probability = float
PredictedWord = tuple[Word, Probability]

UnigramPredicted = PredictedWord
BigramPredicted = dict[str, PredictedWord]
TrigramPredicted = dict[tuple[str, str], PredictedWord]
LeftBigramPredicted = BigramPredicted
RightBigramPredicted = BigramPredicted

Dataset = tuple[UnigramPredicted, LeftBigramPredicted, RightBigramPredicted, TrigramPredicted]

PREDICTED_WORD_INIT = ("", 0.0)

WEIGHT_UNIGRAM = .05
WEIGHT_BIGRAM = .2
WEIGHT_TRIGRAM = .55
WEIGHT_LEFT_BIGRAM = WEIGHT_BIGRAM
WEIGHT_RIGHT_BIGRAM = WEIGHT_BIGRAM

def max_predicted(a: PredictedWord, b: PredictedWord) -> PredictedWord:
    if a[1] > b[1]:
        return a
    return b

def calc_weighted_probability(unigram: Probability = 0.0, leftBigram: Probability = 0.0, rightBigram: Probability = 0.0, trigram: Probability = 0.0) -> Probability:
    return WEIGHT_UNIGRAM * unigram + WEIGHT_LEFT_BIGRAM * leftBigram + WEIGHT_RIGHT_BIGRAM * rightBigram + WEIGHT_TRIGRAM * trigram

def compute_unigram_predicted(unigramProbability: UnigramProbability) -> UnigramPredicted:
    predicted = PREDICTED_WORD_INIT
    for unigram, probability in unigramProbability.items():
        word = unigram[0]

        weightedProbability = calc_weighted_probability(unigram = probability)

        if weightedProbability > predicted[1]:
            predicted = (word, weightedProbability)

    return predicted

# TODO: Combine bigrams into one?
def compute_left_bigram_predicted(unigramProbability: UnigramProbability, leftBigramProbability: LeftBigramProbability) -> LeftBigramPredicted:
    predicted = {}
    for bigram, probability in leftBigramProbability.items():
        prefix = bigram[0]
        word = bigram[1]

        unigram = (bigram[1],)

        weightedProbability = calc_weighted_probability(
            unigram = unigramProbability[unigram], 
            leftBigram = probability
        )

        if not prefix in predicted:
            predicted[prefix] = PREDICTED_WORD_INIT
        if predicted[prefix][1] < weightedProbability:
            predicted[prefix] = (word, weightedProbability)

    return predicted

def compute_right_bigram_predicted(unigramProbability: UnigramProbability, rightBigramProbability: RightBigramProbability) -> RightBigramPredicted:
    predicted = {}
    for bigram, probability in rightBigramProbability.items():
        suffix = bigram[1]
        word = bigram[0]

        unigram = (bigram[0],)

        weightedProbability = calc_weighted_probability(
            unigram = unigramProbability[unigram], 
            rightBigram = probability
        )

        if not suffix in predicted:
            predicted[suffix] = PREDICTED_WORD_INIT
        if predicted[suffix][1] < weightedProbability:
            predicted[suffix] = (word, weightedProbability)

    return predicted

def compute_trigram_predicted(unigramProbability: UnigramProbability, leftBigramProbability: LeftBigramProbability, rightBigramProbability: RightBigramProbability, trigramProbability: TrigramProbability) -> TrigramPredicted:
    predicted = {}
    for trigram, probability in trigramProbability.items():
        ends = (trigram[0], trigram[2])
        word = trigram[1]

        unigram = (trigram[1],)
        leftBigram = (trigram[0], trigram[1])
        rightBigram = (trigram[1], trigram[2])

        weightedProbability = calc_weighted_probability(
            unigram = unigramProbability[unigram],
            leftBigram = leftBigramProbability[leftBigram],
            rightBigram = rightBigramProbability[rightBigram],
            trigram = probability
        )

        if not ends in predicted:
            predicted[ends] = PREDICTED_WORD_INIT
        if predicted[ends][1] < weightedProbability:
            predicted[ends] = (word, weightedProbability)

    return predicted
