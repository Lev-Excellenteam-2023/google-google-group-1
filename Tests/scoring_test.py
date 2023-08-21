import scoring

def test_score_sentence_missing_letter_1():
    input_sentence = 'ello'
    expected_sentence = 'hello'
    assert scoring.score_sentence(input_sentence, expected_sentence) == -2  # 8 - 10

def test_score_sentence_missing_letter_2():
    input_sentence = 'helo'
    expected_sentence = 'hello'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 4  # 8 - 4

def test_score_sentence_wrong_letter_1():
    expected_sentence = 'all thi world'
    input_sentence = 'all the world'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 25  # 26 - -1

def test_score_sentence_wrong_letter_2():
    input_sentence = 'hello'
    expected_sentence = 'bello'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 3  # 8 - 5

def test_score_sentence_wrong_letter_3():
    input_sentence = 'hello'
    expected_sentence = 'hella'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 7  # 8 - 1

def test_score_sentence_extra_letter_1():
    input_sentence = 'helloo'
    expected_sentence = 'hello'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 8  # 10 - 2

def test_score_sentence_extra_letter_2():
    input_sentence = 'helllo'
    expected_sentence = 'hello'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 8  # 10 - 2

def test_score_sentence_extra_letter_3():
    input_sentence = 'i amm good'
    expected_sentence = 'i am good'
    assert scoring.score_sentence(input_sentence, expected_sentence) == 16  # 18 - 2

