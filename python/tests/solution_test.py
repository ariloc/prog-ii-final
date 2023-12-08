from python.src.solution import *

def test_solve_sentences_1():
    """
    Input sentences:
    [
        "ella durmio al calor de las masas",
        "y yo desperte queriendo sonarla",
        "algun tiempo atras pense en escribirle",
        "que nunca sortee las trampas del amor",
        "de aquel amor",
        "de musica ligera",
        "nada nos libra",
        "nada mas queda",
        "no le enviare cenizas de rosas",
        "ni pienso evitar un roce secreto",
        "de aquel amor",
        "de musica ligera",
        "nada nos libra",
        "nada mas queda",
        "de aquel amor",
        "de musica ligera",
        "nada nos libra",
        "nada mas queda",
        "nada mas",
        "nada mas queda",
        "nada mas queda",
        "nada mas queda",
        "nada mas queda",
    ]
    Weights: WEIGHT_UNIGRAM = 0.05, WEIGHT_LEFT_BIGRAM = WEIGHT_RIGHT_BIGRAM = 0.15, WEIGHT_TRIGRAM = 0.65
    """

    unigramPredicted = ('nada', 0.006321839080459771)

    leftBigramPredicted = {
        'ella': ('durmio', 0.15057471264367817), 
        'durmio': ('al', 0.15057471264367817), 
        'al': ('calor', 0.15057471264367817), 
        'calor': ('de', 0.15459770114942528), 
        'de': ('aquel', 0.05797413793103448), 
        'las': ('masas', 0.07557471264367815), 
        'y': ('yo', 0.15057471264367817), 
        'yo': ('desperte', 0.15057471264367817), 
        'desperte': ('queriendo', 0.15057471264367817), 
        'queriendo': ('sonarla', 0.15057471264367817), 
        'algun': ('tiempo', 0.15057471264367817), 
        'tiempo': ('atras', 0.15057471264367817), 
        'atras': ('pense', 0.15057471264367817), 
        'pense': ('en', 0.15057471264367817), 
        'en': ('escribirle', 0.15057471264367817), 
        'que': ('nunca', 0.15057471264367817), 
        'nunca': ('sortee', 0.15057471264367817), 
        'sortee': ('las', 0.1511494252873563), 
        'trampas': ('del', 0.15057471264367817), 
        'del': ('amor', 0.15229885057471265), 
        'aquel': ('amor', 0.15229885057471265), 
        'musica': ('ligera', 0.15172413793103448), 
        'nada': ('mas', 0.11368861024033437), 
        'nos': ('libra', 0.15172413793103448), 
        'mas': ('queda', 0.1540229885057471), 
        'no': ('le', 0.15057471264367817), 
        'le': ('enviare', 0.15057471264367817),
        'enviare': ('cenizas', 0.15057471264367817),
        'cenizas': ('de', 0.15459770114942528), 
        'ni': ('pienso', 0.15057471264367817), 
        'pienso': ('evitar', 0.15057471264367817),
        'evitar': ('un', 0.15057471264367817), 
        'un': ('roce', 0.15057471264367817), 
        'roce': ('secreto', 0.15057471264367817)
    }

    rightBigramPredicted = {
        'durmio': ('ella', 0.15057471264367817),
        'al': ('durmio', 0.15057471264367817), 
        'calor': ('al', 0.15057471264367817), 
        'de': ('calor', 0.07557471264367815),
        'las': ('de', 0.07959770114942528),
        'masas': ('las', 0.1511494252873563),
        'yo': ('y', 0.15057471264367817), 
        'desperte': ('yo', 0.15057471264367817), 
        'queriendo': ('desperte', 0.15057471264367817),
        'sonarla': ('queriendo', 0.15057471264367817), 
        'tiempo': ('algun', 0.15057471264367817), 
        'atras': ('tiempo', 0.15057471264367817), 
        'pense': ('atras', 0.15057471264367817), 
        'en': ('pense', 0.15057471264367817), 
        'escribirle': ('en', 0.15057471264367817), 
        'nunca': ('que', 0.15057471264367817), 
        'sortee': ('nunca', 0.15057471264367817),
        'trampas': ('las', 0.1511494252873563), 
        'del': ('trampas', 0.15057471264367817), 
        'amor': ('aquel', 0.11422413793103448), 
        'aquel': ('de', 0.15459770114942528), 
        'musica': ('de', 0.15459770114942528), 
        'ligera': ('musica', 0.15172413793103448), 
        'nos': ('nada', 0.15632183908045977), 
        'libra': ('nos', 0.15172413793103448), 
        'mas': ('nada', 0.15632183908045977), 
        'queda': ('mas', 0.15459770114942528), 
        'le': ('no', 0.15057471264367817), 
        'enviare': ('le', 0.15057471264367817), 
        'cenizas': ('enviare', 0.15057471264367817),
        'rosas': ('de', 0.15459770114942528), 
        'pienso': ('ni', 0.15057471264367817), 
        'evitar': ('pienso', 0.15057471264367817),
        'un': ('evitar', 0.15057471264367817), 
        'roce': ('un', 0.15057471264367817), 
        'secreto': ('roce', 0.15057471264367817)
    }

    trigramPredicted = {
        ('ella', 'al'): ('durmio', 0.9505747126436782),
        ('durmio', 'calor'): ('al', 0.9505747126436782), 
        ('al', 'de'): ('calor', 0.8755747126436781), 
        ('calor', 'las'): ('de', 0.8795977011494254), 
        ('de', 'masas'): ('las', 0.8198994252873564), 
        ('y', 'desperte'): ('yo', 0.9505747126436782), 
        ('yo', 'queriendo'): ('desperte', 0.9505747126436782), 
        ('desperte', 'sonarla'): ('queriendo', 0.9505747126436782), 
        ('algun', 'atras'): ('tiempo', 0.9505747126436782), 
        ('tiempo', 'pense'): ('atras', 0.9505747126436782), 
        ('atras', 'en'): ('pense', 0.9505747126436782), 
        ('pense', 'escribirle'): ('en', 0.9505747126436782), 
        ('que', 'sortee'): ('nunca', 0.9505747126436782), 
        ('nunca', 'las'): ('sortee', 0.8755747126436781), 
        ('sortee', 'trampas'): ('las', 0.9511494252873564), 
        ('las', 'del'): ('trampas', 0.8755747126436781), 
        ('trampas', 'amor'): ('del', 0.8380747126436782), 
        ('de', 'amor'): ('aquel', 0.8204741379310345),
        ('de', 'ligera'): ('musica', 0.8579741379310345),
        ('nada', 'libra'): ('nos', 0.8426332288401254),
        ('nada', 'queda'): ('mas', 0.9136886102403343),
        ('no', 'enviare'): ('le', 0.9505747126436782),
        ('le', 'cenizas'): ('enviare', 0.9505747126436782),
        ('enviare', 'de'): ('cenizas', 0.8755747126436781),
        ('cenizas', 'rosas'): ('de', 0.9545977011494253),
        ('ni', 'evitar'): ('pienso', 0.9505747126436782),
        ('pienso', 'un'): ('evitar', 0.9505747126436782),
        ('evitar', 'roce'): ('un', 0.9505747126436782), 
        ('un', 'secreto'): ('roce', 0.9505747126436782)
    }

    incompleteSentences = [
        "nada mas _",
        "nada _ queda",
        "_ mas",
        "mas _",
        "nada nos _",
        "_ aquel amor",
        "nunca sortee las _ del amor",
        "y yo desperte _ sonarla",
        "de _ ligera",
        "_ tiempo atras pense en escribirle",
        "_",
        "cenizas _ rosas",
        "poco _ queda",
        "no hay nada mejor que _ libra",
        "me _ cenizas"
    ]

    completedSentences = [
        "nada mas queda",
        "nada mas queda",
        "nada mas",
        "mas queda",
        "nada nos libra",
        "de aquel amor",
        "nunca sortee las trampas del amor",
        "y yo desperte queriendo sonarla",
        "de musica ligera",
        "algun tiempo atras pense en escribirle",
        "nada",
        "cenizas de rosas",
        "poco mas queda",
        "no hay nada mejor que nos libra",
        "me enviare cenizas"
    ]

    dataset = (unigramPredicted, leftBigramPredicted, rightBigramPredicted, trigramPredicted)
    assert solve_sentences(incompleteSentences, dataset) == completedSentences

def test_solve_sentences_2():
    """
    Input sentences:
    [ 
        "buddy you re a boy make a big noise",
        "playing in the street gonna be a big man someday",
        "you got mud on your face you big disgrace",
        "kicking your can all over the place singin",
        "we will we will rock you",
        "we will we will rock you",
        "buddy you re a young man hard man",
        "shouting in the street gonna take on the world someday",
        "you got blood on your face you big disgrace",
        "waving your banner all over the place",
        "we will we will rock you sing it",
        "we will we will rock you",
        "buddy you re an old man poor man",
        "pleading with your eyes gonna make you some peace someday",
        "you got mud on your face big disgrace",
        "somebody better put you back into your place",
        "we will we will rock you sing it",
        "we will we will rock you everybody",
        "we will we will rock you hmm",
        "we will we will rock you",
        "alright"
    ]
    Weights: WEIGHT_UNIGRAM = 0.05, WEIGHT_LEFT_BIGRAM = WEIGHT_RIGHT_BIGRAM = 0.2, WEIGHT_TRIGRAM = 0.55
    """

    unigramPredicted = ('you', 0.0056603773584905665)

    leftBigramPredicted = {
        'buddy': ('you', 0.20566037735849058),
        'you': ('re', 0.04380053908355795), 
        're': ('a', 0.13459119496855346), 
        'a': ('big', 0.10157232704402516), 
        'boy': ('make', 0.20062893081761007), 
        'make': ('you', 0.10566037735849057),
        'big': ('disgrace', 0.12094339622641509), 
        'playing': ('in', 0.20062893081761007), 
        'in': ('the', 0.20157232704402517),
        'the': ('place', 0.08094339622641511),
        'street': ('gonna', 0.2009433962264151),
        'gonna': ('make', 0.06729559748427673),
        'be': ('a', 0.20125786163522014),
        'man': ('someday', 0.06761006289308176),
        'got': ('mud', 0.1339622641509434),
        'mud': ('on', 0.20125786163522014), 
        'on': ('your', 0.15220125786163524), 
        'your': ('face', 0.08665768194070081), 
        'face': ('you', 0.1389937106918239),
        'kicking': ('your', 0.20220125786163523),
        'can': ('all', 0.20062893081761007), 
        'all': ('over', 0.20062893081761007), 
        'over': ('the', 0.20157232704402517), 
        'place': ('singin', 0.20031446540880504),
        'we': ('will', 0.2050314465408805),
        'will': ('we', 0.10503144654088051),
        'rock': ('you', 0.20566037735849058),
        'young': ('man', 0.20157232704402517),
        'hard': ('man', 0.20157232704402517), 
        'shouting': ('in', 0.20062893081761007),
        'take': ('on', 0.20125786163522014), 
        'world': ('someday', 0.2009433962264151), 
        'blood': ('on', 0.20125786163522014), 
        'waving': ('your', 0.20220125786163523),
        'banner': ('all', 0.20062893081761007), 
        'sing': ('it', 0.20062893081761007), 
        'an': ('old', 0.20031446540880504), 
        'old': ('man', 0.20157232704402517), 
        'poor': ('man', 0.20157232704402517),
        'pleading': ('with', 0.20031446540880504),
        'with': ('your', 0.20220125786163523), 
        'eyes': ('gonna', 0.2009433962264151),
        'some': ('peace', 0.20031446540880504),
        'peace': ('someday', 0.2009433962264151),
        'somebody': ('better', 0.20031446540880504),
        'better': ('put', 0.20031446540880504), 
        'put': ('you', 0.20566037735849058), 
        'back': ('into', 0.20031446540880504),
        'into': ('your', 0.20220125786163523)
    }

    rightBigramPredicted = {
        'you': ('rock', 0.10918238993710692),
        're': ('you', 0.20566037735849058), 
        'a': ('re', 0.1009433962264151),
        'boy': ('a', 0.20125786163522014),
        'make': ('gonna', 0.1009433962264151),
        'big': ('you', 0.08566037735849058),
        'noise': ('big', 0.20157232704402517), 
        'in': ('playing', 0.10031446540880504),
        'the': ('in', 0.08062893081761008), 
        'street': ('the', 0.20157232704402517),
        'gonna': ('street', 0.1339622641509434), 
        'be': ('gonna', 0.2009433962264151), 
        'man': ('big', 0.041572327044025165), 
        'someday': ('man', 0.06823899371069182),
        'got': ('you', 0.20566037735849058),
        'mud': ('got', 0.2009433962264151), 
        'on': ('mud', 0.10062893081761007),
        'your': ('on', 0.08697214734950584), 
        'face': ('your', 0.20220125786163523), 
        'disgrace': ('big', 0.20157232704402517),
        'can': ('your', 0.20220125786163523), 
        'all': ('can', 0.10031446540880504), 
        'over': ('all', 0.20062893081761007), 
        'place': ('the', 0.1349056603773585),
        'singin': ('place', 0.2009433962264151), 
        'will': ('we', 0.2050314465408805), 
        'we': ('will', 0.2050314465408805), 
        'rock': ('will', 0.2050314465408805), 
        'young': ('a', 0.20125786163522014), 
        'hard': ('man', 0.20157232704402517), 
        'take': ('gonna', 0.2009433962264151),
        'world': ('the', 0.20157232704402517), 
        'blood': ('got', 0.2009433962264151), 
        'banner': ('your', 0.20220125786163523),
        'sing': ('you', 0.20566037735849058), 
        'it': ('sing', 0.20062893081761007), 
        'an': ('re', 0.2009433962264151), 
        'old': ('an', 0.20031446540880504),
        'poor': ('man', 0.20157232704402517), 
        'with': ('pleading', 0.20031446540880504), 
        'eyes': ('your', 0.20220125786163523), 
        'some': ('you', 0.20566037735849058), 
        'peace': ('some', 0.20031446540880504), 
        'better': ('somebody', 0.20031446540880504),
        'put': ('better', 0.20031446540880504), 
        'back': ('you', 0.20566037735849058), 
        'into': ('back', 0.20031446540880504),
        'everybody': ('you', 0.20566037735849058),
        'hmm': ('you', 0.20566037735849058)
    }

    trigramPredicted = {
        ('buddy', 're'): ('you', 0.9556603773584906),
        ('you', 'a'): ('re', 0.693800539083558),
        ('re', 'boy'): ('a', 0.8845911949685535),
        ('a', 'make'): ('boy', 0.7003144654088052),
        ('boy', 'a'): ('make', 0.8006289308176101),
        ('make', 'big'): ('a', 0.7312578616352202),
        ('a', 'noise'): ('big', 0.8515723270440252),
        ('playing', 'the'): ('in', 0.8306289308176101),
        ('in', 'street'): ('the', 0.9515723270440253),
        ('the', 'gonna'): ('street', 0.7639622641509435),
        ('street', 'be'): ('gonna', 0.9509433962264151),
        ('gonna', 'a'): ('be', 0.6669811320754717),
        ('be', 'big'): ('a', 0.8312578616352202),
        ('a', 'man'): ('big', 0.4165723270440252),
        ('big', 'someday'): ('man', 0.6582389937106918),
        ('you', 'mud'): ('got', 0.7938005390835581),
        ('got', 'on'): ('mud', 0.60062893081761),
        ('mud', 'your'): ('on', 0.8369721473495059),
        ('on', 'face'): ('your', 0.9022012578616353),
        ('your', 'you'): ('face', 0.6633243486073676),
        ('face', 'big'): ('you', 0.768993710691824),
        ('you', 'disgrace'): ('big', 0.7801437556154538),
        ('kicking', 'can'): ('your', 0.9522012578616352),
        ('your', 'all'): ('can', 0.40388589398023367),
        ('can', 'over'): ('all', 0.9506289308176101),
        ('all', 'the'): ('over', 0.8306289308176101),
        ('over', 'place'): ('the', 0.8849056603773585),
        ('the', 'singin'): ('place', 0.8309433962264152),
        ('we', 'we'): ('will', 0.9550314465408806),
        ('will', 'will'): ('we', 0.8550314465408806),
        ('we', 'rock'): ('will', 0.9550314465408806),
        ('will', 'you'): ('rock', 0.759182389937107),
        ('re', 'young'): ('a', 0.8845911949685535),
        ('young', 'hard'): ('man', 0.9515723270440253),
        ('man', 'man'): ('hard', 0.38198113207547174),
        ('shouting', 'the'): ('in', 0.8306289308176101),
        ('street', 'take'): ('gonna', 0.9509433962264151),
        ('gonna', 'on'): ('take', 0.6669811320754717),
        ('take', 'the'): ('on', 0.7912578616352202),
        ('on', 'world'): ('the', 0.8015723270440251),
        ('the', 'someday'): ('world', 0.6569811320754717),
        ('you', 'blood'): ('got', 0.7938005390835581),
        ('blood', 'your'): ('on', 0.8369721473495059),
        ('waving', 'banner'): ('your', 0.9522012578616352),
        ('banner', 'over'): ('all', 0.9506289308176101),
        ('rock', 'sing'): ('you', 0.9556603773584906),
        ('you', 'it'): ('sing', 0.7792003593890386),
        ('you', 'an'): ('re', 0.7938005390835581),
        ('re', 'old'): ('an', 0.8169811320754717),
        ('an', 'man'): ('old', 0.7903144654088051),
        ('old', 'poor'): ('man', 0.9515723270440253),
        ('pleading', 'your'): ('with', 0.7788858939802337),
        ('with', 'eyes'): ('your', 0.9522012578616352),
        ('your', 'gonna'): ('eyes', 0.6455525606469004),
        ('eyes', 'make'): ('gonna', 0.8509433962264151),
        ('gonna', 'you'): ('make', 0.6306289308176101),
        ('make', 'some'): ('you', 0.8556603773584907),
        ('you', 'peace'): ('some', 0.7646001796945194),
        ('some', 'someday'): ('peace', 0.8169811320754717),
        ('your', 'big'): ('face', 0.6766576819407009),
        ('face', 'disgrace'): ('big', 0.8182389937106919),
        ('somebody', 'put'): ('better', 0.9503144654088052),
        ('better', 'you'): ('put', 0.7636477987421384),
        ('put', 'back'): ('you', 0.9556603773584906),
        ('you', 'into'): ('back', 0.7646001796945194),
        ('back', 'your'): ('into', 0.7788858939802337),
        ('into', 'place'): ('your', 0.8188679245283019),
        ('rock', 'everybody'): ('you', 0.9556603773584906),
        ('rock', 'hmm'): ('you', 0.9556603773584906)
    }

    incompleteSentences = [
        "_",
        "_ got mail",
        "_ with us not to do it",
        "big _",
        "we _ rock you",
        "got _ on your face",
        "sing _",
        "will _ will",
        "_",
        "waving _ hand",
        "an old _ told me once",
        "you _ blood on your hands",
        "go _ into your room"
    ]

    completedSentences = [
        "you",
        "you got mail",
        "pleading with us not to do it",
        "big disgrace",
        "we will rock you",
        "got mud on your face",
        "sing it",
        "will we will",
        "you",
        "waving your hand",
        "an old man told me once",
        "you got blood on your hands",
        "go back into your room"
    ]

    dataset = [unigramPredicted, leftBigramPredicted, rightBigramPredicted, trigramPredicted]
    assert solve_sentences(incompleteSentences, dataset) == completedSentences
