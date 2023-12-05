Unigram = tuple[str]
Bigram = tuple[str, str]
Trigram = tuple[str, str, str]
Ngram = tuple[str, ...]

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
