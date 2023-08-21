from variations import check_possible_variations

posible_words = ['alex', 'yehuda', 'omer', 'drive', 'drove', 'yehudi']


def test_check_possible_variations_1():
    assert check_possible_variations('ole', posible_words) == []
    assert check_possible_variations('lex', posible_words) == ['alex']
    assert check_possible_variations('ale', posible_words) == ['alex']
    assert check_possible_variations('almx', posible_words) == ['alex']
    assert check_possible_variations('alx', posible_words) == ['alex']
    assert check_possible_variations('drve', posible_words) == ['drive', 'drove']
    assert check_possible_variations('drave', posible_words) == ['drive', 'drove']
    assert check_possible_variations('yehud', posible_words) == ['yehuda', 'yehudi']
    assert check_possible_variations('yehu', posible_words) == []
    assert check_possible_variations('yehhuda', posible_words) == ['yehuda']
    assert check_possible_variations('yhuda', posible_words) == ['yehuda']
    assert check_possible_variations('yehrda', posible_words) == ['yehuda']

