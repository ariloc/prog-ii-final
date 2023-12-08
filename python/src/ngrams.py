## @file ngrams.py
#  @author Ariel Leonardo Fideleff

Word = str

Ngram = tuple[Word, ...]            
Unigram = tuple[Word]
Bigram = tuple[Word, Word]
Trigram = tuple[Word, Word, Word]

## Extracts and counts how many times a word n-gram occurs among a list of sentences.
#
#  @param sentences A list of sentences where each of the occurring word n-grams will be counted.
#  @param n The size of the word n-gram. For example, if @c n=1, it counts the amount of 
#           <i>unigrams</i> of words in the sentences. However, if @c n=2, it counts the amount of 
#           <i>bigrams</i> of words, and so on.
#  @returns A dictionary containing the count of each n-gram occurring in the sentences.
def extract_ngrams(sentences: list[str], n: int) -> dict[Ngram, int]:
    ngrams = {}
    for sentence in sentences:
        words = sentence.split()
        for i in range(0,len(words)-n+1):
            currentNgram = []
            for j in range(i,i+n):
                currentNgram.append(words[j])

            tupleNgram = tuple(currentNgram)
            if not tupleNgram in ngrams:
                ngrams[tupleNgram] = 0
            ngrams[tupleNgram] += 1

    return ngrams
