from strats import next_fit, fit_first, best_fit

def test_next_fit():
    assert (next_fit([], 42) == 0) # res : []
    assert (next_fit([1], 5) == 1) # res : [{1}]
    assert (next_fit([1,2,3], 3) == 2) # res : [{1,2}, {3}]
    assert (next_fit([1,3,2], 3) == 3) # res : [{1}, {3}, {2}]

def test_fit_first():
    assert (fit_first([], 42) == 0) # res : []
    assert (fit_first([1], 5) == 1) # res : [{1}]
    assert (fit_first([1,2,3], 3) == 2) # res : [{1,2}, {3}]
    assert (fit_first([1,3,2], 3) == 2) # res : [{1,2}, {3}]
    assert (fit_first([3,4,1,2], 5) == 3) # res : [{3,1}, {4}, {2}]

def test_best_fit():
    assert (best_fit([], 42) == 0) # res : []
    assert (best_fit([1], 5) == 1) # res : [{1}]
    assert (best_fit([1,2,3], 3) == 2) # res : [{1,2}, {3}]
    assert (best_fit([1,3,2], 3) == 2) # res : [{1,2}, {3}]
    assert (best_fit([3,4,1,2], 5) == 2) # res : [{3,2}, {4,1}]

test_next_fit()
test_fit_first()
test_best_fit()
