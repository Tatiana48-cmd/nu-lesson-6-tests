from functions_t import filter_odd_num, plus

def test_filter_odd_num():
    assert filter_odd_num('numbers') == [2, 4, 8, 10]

def test_plus():
    assert plus('numbers') == 48

def test_map():
    assert map(plus, 'numbers') == [48]

def test_sorted():
    assert sorted == [11, 10, 8, 7, 5, 4, 2, 1]