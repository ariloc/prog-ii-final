from .predictions import max_predicted, Dataset

def solve_sentences(sentences: list[str], dataset: Dataset) -> list[str]:
    (unigramPredicted, leftBigramPredicted, rightBigramPredicted, trigramPredicted) = dataset

    solved = []

    for sentence in sentences:
        words = sentence.split()
        wordCount = len(words)

        # Only non empty strings
        if words:
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
