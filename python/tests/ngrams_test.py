from python.src.ngrams import *

def test_unigram():
    sentences = [
        "one",
        "two three",
        "four five six",
        "  seven   eight   nine  ",
        "nine  ",
        "   seven",
        "eight eight eight eight",
        "eight",
        ""
    ]
    expectedDict = {
        ("one",): 1,
        ("two",): 1,
        ("three",): 1,
        ("four",): 1,
        ("five",): 1,
        ("six",): 1,
        ("seven",): 2,
        ("eight",): 6,
        ("nine",): 2
    }
    assert extract_ngrams(sentences, 1) == expectedDict

def test_bigram():
    sentences = [
        "",
        "this is a test",
        "a test this is",
        "testing testing testing",
        "testing",
        "the test",
    ]
    expectedDict = {
        ("this", "is"): 2,
        ("is", "a"): 1,
        ("a", "test"): 2,
        ("test", "this"): 1,
        ("testing", "testing"): 2,
        ("the", "test"): 1
    }
    assert extract_ngrams(sentences, 2) == expectedDict

def test_trigram():
    sentences = [
        "tres tristes tigres comieron trigo en un trigal",
        "three short words",
        "un trigal inmenso",
        "los tigres comieron trigo",
        "",
        "el y ella",
        "el y",
        "ella y",
        "el",
        "ella",
        "el y ella se vieron",
        "el y ella se conocieron",
    ]
    expectedDict = {
        ("tres", "tristes", "tigres"): 1,
        ("tristes", "tigres", "comieron"): 1,
        ("tigres", "comieron", "trigo"): 2,
        ("comieron", "trigo", "en"): 1,
        ("trigo", "en", "un"): 1,
        ("en", "un", "trigal"): 1,
        ("three", "short", "words"): 1,
        ("un", "trigal", "inmenso"): 1,
        ("los", "tigres", "comieron"): 1,
        ("el", "y", "ella"): 3,
        ("y", "ella", "se"): 2,
        ("ella", "se", "vieron"): 1,
        ("ella", "se", "conocieron"): 1
    }
    assert extract_ngrams(sentences, 3) == expectedDict

def test_7gram():
    sentences = [
        "",
        "hola",
        "hola mundo",
        "hola mundo bonito",
        "hola mundo bonito y",
        "hola mundo bonito y hermoso",
        "hola mundo bonito y hermoso que",
        "hola mundo bonito y hermoso que tal",
        "hola mundo bonito y hermoso que tal como",
        "hola mundo bonito y hermoso que tal como estas"
    ]
    expectedDict = {
        ("hola", "mundo", "bonito", "y", "hermoso", "que", "tal"): 3,
        ("mundo", "bonito", "y", "hermoso", "que", "tal", "como"): 2,
        ("bonito", "y", "hermoso", "que", "tal", "como", "estas"): 1
    }
    assert extract_ngrams(sentences, 7) == expectedDict
