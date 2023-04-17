def some_f(n):
    return n*20

print(some_f(20))

assert some_f(20) == 400

def test_1():
    actual = [1, 2, 3]
    expected = [1, 2, 4]
    assert expected == actual

def test_2():
    actual = [1, 2, 3]
    expected = [1, 2, 4]
    if actual != expected:
        raise AssertionError("Actual and expected are not equal")