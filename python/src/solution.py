## @file solution.py
#  @author Ariel Leonardo Fideleff

from .predictions import max_predicted, Dataset

## Fills in missing words in a list of sentences written by a person, given a precomputed 
#  predictions @link python.src.predictions.Dataset Dataset@endlink generated from sentences written
#  by the person.
#
#  Each of the sentences received as an argument <b>must</b> have an underscore (@p '_'), 
#  representing the location of the missing word.
#
#  @param sentences A list of sentences with missing words written by a person to be completed.
#  @param dataset A precomputed dataset generated from sentences written by the person.
#  @return The list of completed sentences.
def solve_sentences(sentences: list[str], dataset: Dataset) -> list[str]:
    (unigramPredicted, leftBigramPredicted, rightBigramPredicted, trigramPredicted) = dataset

    solved = []

    for sentence in sentences:
        words = sentence.split()
        wordCount = len(words)

        # Assuming there's always a single '_' word
        underscorePosition = words.index("_")
        
        predictedWord = unigramPredicted

        if underscorePosition < wordCount-1 and words[underscorePosition+1] in rightBigramPredicted:
            predictedWord = max_predicted(predictedWord, rightBigramPredicted[words[underscorePosition+1]])

        if underscorePosition > 0 and words[underscorePosition-1] in leftBigramPredicted:
            predictedWord = max_predicted(predictedWord, leftBigramPredicted[words[underscorePosition-1]])
            
        if underscorePosition > 0 and underscorePosition < wordCount-1:
            adjacentTuple = (words[underscorePosition-1], words[underscorePosition+1])
            if adjacentTuple in trigramPredicted:
                predictedWord = max_predicted(predictedWord, trigramPredicted[adjacentTuple])

        words[underscorePosition] = predictedWord[0]
        solved.append(' '.join(words))

    return solved
