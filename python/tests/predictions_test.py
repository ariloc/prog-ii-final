import pytest

import python.src.predictions
from python.src.predictions import *

# Helper function
def patch_weights(monkeypatch, unigram: float, leftBigram: float, rightBigram: float, trigram: float):
    # Patch global variables for testing
    monkeypatch.setattr(python.src.predictions, "WEIGHT_UNIGRAM", unigram)
    monkeypatch.setattr(python.src.predictions, "WEIGHT_LEFT_BIGRAM", leftBigram)
    monkeypatch.setattr(python.src.predictions, "WEIGHT_RIGHT_BIGRAM", rightBigram)
    monkeypatch.setattr(python.src.predictions, "WEIGHT_TRIGRAM", trigram)

# Tests
def test_calc_score(monkeypatch):
    patch_weights(monkeypatch, unigram = .1, leftBigram = .15, rightBigram = .25, trigram = .5)
    assert calc_score(.23, .15, .11, .08) == pytest.approx(.113)

def test_compute_unigram_predicted_1(monkeypatch):
    patch_weights(monkeypatch, unigram = .075, leftBigram = .216, rightBigram = .109, trigram = .6)

    unigramProbability = {
        ('pepe',): .21739130434782608,
        ('pepito',): .17391304347826086,
        ('paco',): .13043478260869565,
        ('paquito',): .17391304347826086,
        ('mundo',): .13043478260869565, 
        ('hola',): .17391304347826086
    }
    predicted = ('pepe', pytest.approx(.0163043478))
    assert compute_unigram_predicted(unigramProbability) == predicted

def test_compute_unigram_predicted_2(monkeypatch):
    patch_weights(monkeypatch, unigram = .05, leftBigram = .25, rightBigram = .18, trigram = .52)

    unigramProbability = {
        ('pc',): 0.3333333333333333,
        ('tv',): 0.3333333333333333,
        ('hola',): 0.16666666666666666, 
        ('mundo',): 0.08333333333333333,
        ('pepe',): 0.08333333333333333
    }
    predicted1 = ("pc", pytest.approx(0.016666666665))
    predicted2 = ("tv", pytest.approx(0.016666666665))
    predictedAssert = compute_unigram_predicted(unigramProbability) 
    assert predictedAssert == predicted1 or predictedAssert == predicted2

def test_compute_left_bigram_predicted(monkeypatch):
    patch_weights(monkeypatch, unigram = .075, leftBigram = .225, rightBigram = .2, trigram = .5)

    leftBigramProbability = {
        ('es', 'unico'): 0.25, 
        ('es', 'particular'): 0.125,
        ('es', 'especial'): 0.25,
        ('es', 'interesante'): 0.125,
        ('es', 'bello'): 0.25,
        ('ser', 'particular'): 0.9787234042553191,
        ('ser', 'interesante'): 0.02127659574468085
    }

    unigramProbability = {
        ('es',): 0.07272727272727272, 
        ('unico',): 0.01818181818181818, 
        ('particular',): 0.42727272727272725,
        ('especial',): 0.01818181818181818,
        ('interesante',): 0.01818181818181818,
        ('bello',): 0.01818181818181818,
        ('ser',): 0.42727272727272725
    }

    predicted = {
        "es": ("particular", pytest.approx(0.0601704545)),
        "ser": ("particular", pytest.approx(0.252258221))
    }

    assert compute_left_bigram_predicted(unigramProbability, leftBigramProbability) == predicted

def test_compute_right_bigram_predicted(monkeypatch):
    patch_weights(monkeypatch, unigram = .025, leftBigram = .2, rightBigram = .25, trigram = .525)

    rightBigramProbability = {
        ('buen', 'vino'): 0.4166666666666667,
        ('mal', 'vino'): 0.08333333333333333, 
        ('poco', 'vino'): 0.16666666666666666, 
        ('mucho', 'vino'): 0.08333333333333333,
        ('escaso', 'vino'): 0.08333333333333333, 
        ('feo', 'vino'): 0.16666666666666666, 
        ('gran', 'ventana'): 0.16666666666666666,
        ('pequena', 'ventana'): 0.08333333333333333, 
        ('alta', 'ventana'): 0.08333333333333333,
        ('corta', 'ventana'): 0.08333333333333333,
        ('ancha', 'ventana'): 0.3333333333333333, 
        ('estrecha', 'ventana'): 0.25,
        ('terrible', 'idea'): 0.17647058823529413,
        ('pesima', 'idea'): 0.11764705882352941, 
        ('buena', 'idea'): 0.17647058823529413,
        ('mala', 'idea'): 0.11764705882352941,
        ('una', 'idea'): 0.11764705882352941, 
        ('otra', 'idea'): 0.29411764705882354
    }

    unigramProbability = {
        ('buen',): 0.06097560975609756,
        ('vino',): 0.14634146341463414, 
        ('mal',): 0.012195121951219513, 
        ('poco',): 0.024390243902439025, 
        ('mucho',): 0.012195121951219513,
        ('escaso',): 0.012195121951219513,
        ('feo',): 0.024390243902439025,
        ('gran',): 0.024390243902439025,
        ('ventana',): 0.14634146341463414, 
        ('pequena',): 0.012195121951219513,
        ('alta',): 0.012195121951219513,
        ('corta',): 0.012195121951219513, 
        ('ancha',): 0.04878048780487805, 
        ('estrecha',): 0.036585365853658534, 
        ('terrible',): 0.036585365853658534, 
        ('idea',): 0.2073170731707317, 
        ('pesima',): 0.024390243902439025,
        ('buena',): 0.036585365853658534,
        ('mala',): 0.024390243902439025, 
        ('una',): 0.024390243902439025,
        ('otra',): 0.06097560975609756
    }

    predicted = {
        "vino": ("buen", pytest.approx(0.105691057)),
        "ventana": ("ancha", pytest.approx(0.0845528455)),
        "idea": ("otra", pytest.approx(0.075053802))
    }

    assert compute_right_bigram_predicted(unigramProbability, rightBigramProbability) == predicted

def test_compute_trigram_predicted(monkeypatch):
    patch_weights(monkeypatch, unigram = .05, leftBigram = .2, rightBigram = .21, trigram = .54)

    trigramProbability = {
        ('un', 'bello', 'mundo'): 0.08333333333333333, 
        ('un', 'lindo', 'mundo'): 0.08333333333333333,
        ('un', 'simple', 'mundo'): 0.25, 
        ('un', 'interesante', 'mundo'): 0.08333333333333333, 
        ('un', 'pacifico', 'mundo'): 0.4166666666666667,
        ('un', 'mundo', 'normal'): 0.0625, 
        ('un', 'pez', 'normal'): 0.25,
        ('un', 'camello', 'normal'): 0.125,
        ('un', 'perro', 'normal'): 0.1875, 
        ('un', 'caballo', 'normal'): 0.3125, 
        ('un', 'oso', 'normal'): 0.0625, 
        ('un', 'gran', 'mundo'): 0.08333333333333333, 
        ('muy', 'buen', 'mundo'): 0.05555555555555555, 
        ('muy', 'mal', 'mundo'): 0.05555555555555555, 
        ('muy', 'pesimo', 'mundo'): 0.2222222222222222, 
        ('muy', 'excelente', 'mundo'): 0.16666666666666666, 
        ('muy', 'decente', 'mundo'): 0.16666666666666666,
        ('muy', 'mediocre', 'mundo'): 0.3333333333333333
    }

    leftBigramProbability = {
        ('un', 'bello'): 0.03571428571428571, 
        ('bello', 'mundo'): 1.0, 
        ('un', 'lindo'): 0.03571428571428571, 
        ('lindo', 'mundo'): 1.0, 
        ('un', 'simple'): 0.10714285714285714,
        ('simple', 'mundo'): 1.0,
        ('un', 'interesante'): 0.03571428571428571, 
        ('interesante', 'mundo'): 1.0,
        ('un', 'pacifico'): 0.17857142857142858, 
        ('pacifico', 'mundo'): 1.0, 
        ('un', 'mundo'): 0.03571428571428571, 
        ('mundo', 'normal'): 1.0, 
        ('un', 'pez'): 0.14285714285714285, 
        ('pez', 'normal'): 1.0, 
        ('un', 'camello'): 0.07142857142857142, 
        ('camello', 'normal'): 1.0, 
        ('un', 'perro'): 0.10714285714285714, 
        ('perro', 'normal'): 1.0, 
        ('un', 'caballo'): 0.17857142857142858,
        ('caballo', 'normal'): 1.0, 
        ('un', 'oso'): 0.03571428571428571, 
        ('oso', 'normal'): 1.0, 
        ('un', 'gran'): 0.03571428571428571,
        ('gran', 'mundo'): 1.0, 
        ('muy', 'buen'): 0.05555555555555555,
        ('buen', 'mundo'): 1.0,
        ('muy', 'mal'): 0.05555555555555555,
        ('mal', 'mundo'): 1.0,
        ('muy', 'pesimo'): 0.2222222222222222,
        ('pesimo', 'mundo'): 1.0, 
        ('muy', 'excelente'): 0.16666666666666666,
        ('excelente', 'mundo'): 1.0, 
        ('muy', 'decente'): 0.16666666666666666,
        ('decente', 'mundo'): 1.0, 
        ('muy', 'mediocre'): 0.3333333333333333, 
        ('mediocre', 'mundo'): 1.0
    }

    rightBigramProbability = {
        ('un', 'bello'): 1.0, 
        ('bello', 'mundo'): 0.03225806451612903, 
        ('un', 'lindo'): 1.0, 
        ('lindo', 'mundo'): 0.03225806451612903, 
        ('un', 'simple'): 1.0, 
        ('simple', 'mundo'): 0.0967741935483871,
        ('un', 'interesante'): 1.0, 
        ('interesante', 'mundo'): 0.03225806451612903, 
        ('un', 'pacifico'): 1.0,
        ('pacifico', 'mundo'): 0.16129032258064516, 
        ('un', 'mundo'): 0.03225806451612903,
        ('mundo', 'normal'): 0.0625, 
        ('un', 'pez'): 1.0,
        ('pez', 'normal'): 0.25,
        ('un', 'camello'): 1.0, 
        ('camello', 'normal'): 0.125, 
        ('un', 'perro'): 1.0,
        ('perro', 'normal'): 0.1875, 
        ('un', 'caballo'): 1.0,
        ('caballo', 'normal'): 0.3125,
        ('un', 'oso'): 1.0, 
        ('oso', 'normal'): 0.0625, 
        ('un', 'gran'): 1.0, 
        ('gran', 'mundo'): 0.03225806451612903, 
        ('muy', 'buen'): 1.0, 
        ('buen', 'mundo'): 0.03225806451612903, 
        ('muy', 'mal'): 1.0, 
        ('mal', 'mundo'): 0.03225806451612903, 
        ('muy', 'pesimo'): 1.0, 
        ('pesimo', 'mundo'): 0.12903225806451613,
        ('muy', 'excelente'): 1.0, 
        ('excelente', 'mundo'): 0.0967741935483871,
        ('muy', 'decente'): 1.0, 
        ('decente', 'mundo'): 0.0967741935483871,
        ('muy', 'mediocre'): 1.0, 
        ('mediocre', 'mundo'): 0.1935483870967742
    }

    unigramProbability = {
        ('un',): 0.2028985507246377,
        ('bello',): 0.007246376811594203,
        ('mundo',): 0.2246376811594203, 
        ('lindo',): 0.007246376811594203,
        ('simple',): 0.021739130434782608,
        ('interesante',): 0.007246376811594203,
        ('pacifico',): 0.036231884057971016,
        ('normal',): 0.11594202898550725,
        ('pez',): 0.028985507246376812, 
        ('camello',): 0.014492753623188406,
        ('perro',): 0.021739130434782608,
        ('caballo',): 0.036231884057971016,
        ('oso',): 0.007246376811594203,
        ('gran',): 0.007246376811594203, 
        ('muy',): 0.13043478260869565, 
        ('buen',): 0.007246376811594203,
        ('mal',): 0.007246376811594203,
        ('pesimo',): 0.028985507246376812, 
        ('excelente',): 0.021739130434782608,
        ('decente',): 0.021739130434782608, 
        ('mediocre',): 0.043478260869565216
    }

    predicted = {
        ("un", "mundo"): ("pacifico", pytest.approx(0.296396848)),
        ("un", "normal"): ("caballo", pytest.approx(0.27190088)),
        ("muy", "mundo"): ("mediocre", pytest.approx(0.289485656)),
    }

    assert compute_trigram_predicted(unigramProbability, leftBigramProbability, rightBigramProbability, trigramProbability) == predicted
