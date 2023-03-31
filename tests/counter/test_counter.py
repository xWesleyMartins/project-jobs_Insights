from src.pre_built.counter import count_ocurrences


def test_counter():
    word_js_count = count_ocurrences("data/jobs.csv", "javascript")
    word_py_count = count_ocurrences("data/jobs.csv", "Python")

    assert word_js_count == 122
    assert word_py_count == 1639
