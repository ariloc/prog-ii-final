## @file predictions.py
#  @author Ariel Leonardo Fideleff

from .probability import UnigramProbability, LeftBigramProbability, RightBigramProbability, TrigramProbability, Probability
from .ngrams import Word

Score = float
PredictedWord = tuple[Word, Score]

UnigramPredicted = PredictedWord
BigramPredicted = dict[Word, PredictedWord]
TrigramPredicted = dict[tuple[Word, Word], PredictedWord]
LeftBigramPredicted = BigramPredicted
RightBigramPredicted = BigramPredicted

## A tuple containing precomputed predicted words given a certain word unigram, left/right bigram 
#  or trigram.
#
#  @see @link python.src.predictions.compute_unigram_predicted() compute_unigram_predicted() 
#       @endlink
#  @see @link python.src.predictions.compute_left_bigram_predicted() compute_left_bigram_predicted() 
#       @endlink
#  @see @link python.src.predictions.compute_right_bigram_predicted() compute_right_bigram_predicted() 
#       @endlink
#  @see @link python.src.predictions.compute_trigram_predicted() compute_trigram_predicted() 
#       @endlink
Dataset = tuple[UnigramPredicted, LeftBigramPredicted, RightBigramPredicted, TrigramPredicted]

## Default value for a @p PredictedWord type
PREDICTED_WORD_INIT: PredictedWord = ("", 0.0)

WEIGHT_UNIGRAM = .05
WEIGHT_BIGRAM = .2
WEIGHT_LEFT_BIGRAM = WEIGHT_BIGRAM
WEIGHT_RIGHT_BIGRAM = WEIGHT_BIGRAM
WEIGHT_TRIGRAM = .55


## Given two predicted words, compares and returns the one with the higher @p Score. 
#  If both have the same score, then any of the two is valid.
#
#  @param a The first predicted word to be compared.
#  @param b The second predicted word to be compared.
#  @return The predicted word with the highest score.
def max_predicted(a: PredictedWord, b: PredictedWord) -> PredictedWord:
    if a[1] > b[1]:
        return a
    return b

## Calculates the @p Score for a word @f$W_i^j@f$ (for each @f$j = 1,2,\dots,n@f$, where @f$n@f$ 
#  is the amount of distinct words in the corpus) to be used as a replacement for the missing word
#  in a trigram starting in @f$W_{i-1}@f$ and ending with @f$W_{i+1}@f$.
#
#  To calculate the score, the function requires the probabilities of
#  the unigram @f$(W_i)@f$, the left and right bigrams, @f$(W_{i-1} W_i^j)@f$ and 
#  @f$(W_i^j W_{i+1}^j)@f$ respectively, and the trigram @f$(W_{i-1} W_i^j W_{i+1})@f$,
#  in a list of sentences.
#  
#  This score is calculated based on certain fixed weights @f$ \lambda_1 = @f$ 
#  @link python.src.predictions.WEIGHT_UNIGRAM WEIGHT_UNIGRAM@endlink, @f$ \lambda_2 = @f$
#  @link python.src.predictions.WEIGHT_LEFT_BIGRAM WEIGHT_LEFT_BIGRAM@endlink, @f$ \lambda_3 = @f$
#  @link python.src.predictions.WEIGHT_RIGHT_BIGRAM WEIGHT_RIGHT_BIGRAM@endlink and 
#  @f$ \lambda_4 = @f$ @link python.src.predictions.WEIGHT_TRIGRAM WEIGHT_TRIGRAM@endlink where
#  @f$\lambda_1 + \lambda_2 + \lambda_3 + \lambda_4 = 1@f$:
#
#  @f[ \text{Score}(W_i^j) = \lambda_1 \text{P}(W_i^j) + \lambda_2 \text{P}(W_i^j|W_{i-1}) + 
#                            \lambda_3 \text{P}(W_i^j|W_{i+1}) + 
#                            \lambda_4 \text{P}(W_i^j|W_{i-1},W_{i+1}) @f]
#
#  <i>May also be used to calculate the score for bigrams or unigrams with the missing probabilities 
#  (of the longer n-grams) left as @c 0.0.</i>
#
#  @param unigram The probability of the unigram @f$(W_i^j)@f$, i.e. the frequency of the word 
#                 @f$W_i^j@f$ in the corpus.
#  @param leftBigram The probability of the left bigram @f$(W_{i-1} W_i^j)@f$.
#  @param rightBigram The probability of the right bigram @f$(W_i^j W_{i+1})@f$.
#  @param trigram The probability of the trigram @f$(W_{i-1} W_i^j W_{i+1})@f$.
#  @return The score for the word @f$W_i^j@f$ to be predicted as a replacement for the missing word
#          in a trigram @f$(W_{i-1} W_i^j W_{i+1})@f$.
#
#  @see @link python.src.probability.compute_unigram_probability() compute_unigram_probability() 
#       @endlink
#  @see @link python.src.probability.compute_left_bigram_probability() 
#             compute_left_bigram_probability() @endlink
#  @see @link python.src.probability.compute_right_bigram_probability() 
#             compute_right_bigram_probability() @endlink
#  @see @link python.src.probability.compute_trigram_probability() compute_trigram_probability() 
#       @endlink
def calc_score(unigram: Probability = 0.0, leftBigram: Probability = 0.0, rightBigram: Probability = 0.0, trigram: Probability = 0.0) -> Score:
    return WEIGHT_UNIGRAM * unigram + WEIGHT_LEFT_BIGRAM * leftBigram + WEIGHT_RIGHT_BIGRAM * rightBigram + WEIGHT_TRIGRAM * trigram

## Computes the predicted word with the highest @p Score among all unigrams in a list of sentences.
#
#  @param unigramProbability The probability of all unigrams in a certain list of sentences.
#  @return A predicted word with the highest score.
#
#  @see @link python.src.predictions.calc_score() calc_score() @endlink
#  @see @link python.src.probability.compute_unigram_probability() compute_unigram_probability() 
#       @endlink
def compute_unigram_predicted(unigramProbability: UnigramProbability) -> UnigramPredicted:
    predicted = PREDICTED_WORD_INIT
    for unigram, probability in unigramProbability.items():
        word = unigram[0]

        score = calc_score(unigram = probability)

        if predicted[1] < score:
            predicted = (word, score)

    return predicted

## Computes the predicted word with the highest @p Score among all bigrams that <i>start</i> with 
#  a certain word in a list of sentences.
#
#  @param unigramProbability The probability for each of the unigrams in a list of sentences.
#  @param leftBigramProbability The probability for each of the left bigrams in a list of sentences.
#  @return A dictionary containing the predicted word with the best score for each of the bigrams
#          <i>starting</i> in a given word.
#
#  @see @link python.src.predictions.calc_score() calc_score() @endlink
#  @see @link python.src.probability.compute_unigram_probability() compute_unigram_probability() 
#       @endlink
#  @see @link python.src.probability.compute_left_bigram_probability() 
#             compute_left_bigram_probability() @endlink
def compute_left_bigram_predicted(unigramProbability: UnigramProbability, leftBigramProbability: LeftBigramProbability) -> LeftBigramPredicted:
    predicted = {}
    for bigram, probability in leftBigramProbability.items():
        prefix = bigram[0]
        word = bigram[1]

        unigram = (bigram[1],)

        score = calc_score(
            unigram = unigramProbability[unigram], 
            leftBigram = probability
        )

        if not prefix in predicted:
            predicted[prefix] = PREDICTED_WORD_INIT
        if predicted[prefix][1] < score:
            predicted[prefix] = (word, score)

    return predicted

## Computes the predicted word with the highest @p Score among all bigrams that <i>end</i> with 
#  a certain word in a list of sentences.
#
#  @param unigramProbability The probability for each of the unigrams in a list of sentences.
#  @param rightBigramProbability The probability for each of the right bigrams in a list of sentences.
#  @return A dictionary containing the predicted word with the best score for each of the bigrams
#          <i>ending</i> in a given word.
#
#  @see @link python.src.predictions.calc_score() calc_score() @endlink
#  @see @link python.src.probability.compute_unigram_probability() compute_unigram_probability() 
#       @endlink
#  @see @link python.src.probability.compute_right_bigram_probability() 
#             compute_right_bigram_probability() @endlink
def compute_right_bigram_predicted(unigramProbability: UnigramProbability, rightBigramProbability: RightBigramProbability) -> RightBigramPredicted:
    predicted = {}
    for bigram, probability in rightBigramProbability.items():
        suffix = bigram[1]
        word = bigram[0]

        unigram = (bigram[0],)

        score = calc_score(
            unigram = unigramProbability[unigram], 
            rightBigram = probability
        )

        if not suffix in predicted:
            predicted[suffix] = PREDICTED_WORD_INIT
        if predicted[suffix][1] < score:
            predicted[suffix] = (word, score)

    return predicted

## Computes the predicted word with the highest @p Score among all bigrams that <i>start and end</i>
#  with a pair of words in a list of sentences.
#
#  @param unigramProbability The probability for each of the unigrams in a list of sentences.
#  @param leftBigramProbability The probability for each of the left bigrams in a list of sentences.
#  @param rightBigramProbability The probability for each of the right bigrams in a list of sentences.
#  @param trigramProbability The probability for each of the trigrams in a list of sentences.
#  @return A dictionary containing the predicted word with the best score for each of the bigrams
#          <i>starting and ending</i> in two given words.
#
#  @see @link python.src.predictions.calc_score() calc_score() @endlink
#  @see @link python.src.probability.compute_unigram_probability() compute_unigram_probability() 
#       @endlink
#  @see @link python.src.probability.compute_left_bigram_probability() 
#             compute_left_bigram_probability() @endlink
#  @see @link python.src.probability.compute_right_bigram_probability() 
#             compute_right_bigram_probability() @endlink
#  @see @link python.src.probability.compute_trigram_probability() 
#             compute_trigram_probability() @endlink
def compute_trigram_predicted(unigramProbability: UnigramProbability, leftBigramProbability: LeftBigramProbability, rightBigramProbability: RightBigramProbability, trigramProbability: TrigramProbability) -> TrigramPredicted:
    predicted = {}
    for trigram, probability in trigramProbability.items():
        ends = (trigram[0], trigram[2])
        word = trigram[1]

        unigram = (trigram[1],)
        leftBigram = (trigram[0], trigram[1])
        rightBigram = (trigram[1], trigram[2])

        score = calc_score(
            unigram = unigramProbability[unigram],
            leftBigram = leftBigramProbability[leftBigram],
            rightBigram = rightBigramProbability[rightBigram],
            trigram = probability
        )

        if not ends in predicted:
            predicted[ends] = PREDICTED_WORD_INIT
        if predicted[ends][1] < score:
            predicted[ends] = (word, score)

    return predicted
