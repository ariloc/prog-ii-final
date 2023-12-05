import pytest

from python.src.probability import *

def test_compute_unigram_probability():
    unigrams = {
        ("hello",): 3,
        ("bye",): 7,
        ("test",): 2,
        ("other",): 1,
        ("lots",): 11
    }
    expectedProb = {
        ("hello",): pytest.approx(.125),
        ("bye",): pytest.approx(.291666667),
        ("test",): pytest.approx(.083333333),
        ("other",): pytest.approx(.041666667),
        ("lots",): pytest.approx(.458333333)
    }
    assert compute_unigram_probability(unigrams) == expectedProb

def test_compute_left_bigram_probability():
    bigrams = {
        ("hello", "world"): 2,
        ("hello", "dad"): 4,
        ("hello", "you"): 1,
        ("my", "day"): 7,
        ("my", "tv"): 2,
        ("my", "phone"): 4,
        ("my", "investigation"): 1,
        ("a", "test"): 1,
        ("a", "tester"): 1,
        ("lone", "bigram"): 3
    }
    expectedProb = {
        ("hello", "world"): pytest.approx(.285714286),
        ("hello", "dad"): pytest.approx(.571428571),
        ("hello", "you"): pytest.approx(.142857143),
        ("my", "day"): pytest.approx(.5),
        ("my", "tv"): pytest.approx(.142857143),
        ("my", "phone"): pytest.approx(.285714286),
        ("my", "investigation"): pytest.approx(.0714285714),
        ("a", "test"): pytest.approx(.5),
        ("a", "tester"): pytest.approx(.5),
        ("lone", "bigram"): pytest.approx(1)
    }
    assert compute_left_bigram_probability(bigrams) == expectedProb

def test_compute_right_bigram_probability():
    bigrams = {
        ("triste", "gato"): 2,
        ("feliz", "gato"): 4,
        ("buen", "perro"): 8,
        ("pocos", "animales"): 1,
        ("muchos", "animales"): 2,
        ("demasiados", "animales"): 5,
        ("escasos", "animales"): 3,
        ("un", "dia"): 3,
        ("el", "dia"): 3
    }
    expectedProb = {
        ("triste", "gato"): pytest.approx(.333333333),
        ("feliz", "gato"): pytest.approx(.666666667),
        ("buen", "perro"): pytest.approx(1),
        ("pocos", "animales"): pytest.approx(.0909090909),
        ("muchos", "animales"): pytest.approx(.181818182),
        ("demasiados", "animales"): pytest.approx(.454545455),
        ("escasos", "animales"): pytest.approx(.272727273),
        ("un", "dia"): pytest.approx(.5),
        ("el", "dia"): pytest.approx(.5)
    }
    assert compute_right_bigram_probability(bigrams) == expectedProb

def test_compute_trigram_probability():
    trigrams = {
        ("tres", "tristes", "tigres"): 3,
        ("tres", "felices", "tigres"): 3,
        ("de", "noche", "y"): 1,
        ("de", "dia", "y"): 5,
        ("de", "tarde", "y"): 2,
        ("de", "noche", "calurosa"): 2,
        ("pero", "no", "puede"): 8,
        ("pero", "si", "puede"): 3,
        ("pero", "capaz", "puede"): 1,
        ("pero", "siempre", "puede"): 11
    }
    expectedProb = {
        ("tres", "tristes", "tigres"): pytest.approx(.5),
        ("tres", "felices", "tigres"): pytest.approx(.5),
        ("de", "noche", "y"): pytest.approx(.125),
        ("de", "dia", "y"): pytest.approx(.625),
        ("de", "tarde", "y"): pytest.approx(.25),
        ("de", "noche", "calurosa"): pytest.approx(1),
        ("pero", "no", "puede"): pytest.approx(.347826086),
        ("pero", "si", "puede"): pytest.approx(.130434782),
        ("pero", "capaz", "puede"): pytest.approx(.043478260),
        ("pero", "siempre", "puede"): pytest.approx(.478260869)
    }
    assert compute_trigram_probability(trigrams) == expectedProb
