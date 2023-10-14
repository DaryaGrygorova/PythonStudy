"""
Tests are comprised of the following components:
1. Inputs
2. Result tested function
    2.1. Prepare the initial state of the system
    2.2. Run our tested function with inputs
3. Testing function (comparing expected to actual)
4. Cleanup
"""
import ex1


def test_counter1():
    # у цій реалізації тест буде пройдений навіть для "зафейлених" випадків
    """Test func for count_min_replacements"""
    for arr, res in MY_TESTCASE:
        try:
            assert ex1.count_min_replacements(arr) == res
        except AssertionError:
            print("failed: ", arr, res)


def test_counter2():
    # у цій реалізації весь тест буде "зафейлений" на першій же помилці.
    # Інші кейси не будуть запущені
    """Test func for count_min_replacements"""
    for arr, res in MY_TESTCASE:
        assert ex1.count_min_replacements(arr) == res


def counter_tests_generator():
    """Generator for test func for count_min_replacements"""
    # BadCase(маніпуляція з globals).
    # Генератор буде створювати у глобальній області видимості
    # нову тестову функцію для кожного кейсу з MY_TESTCASES
    for index, (arr, res) in enumerate(MY_TESTCASE):

        def generate_test(array, result):  # створення замикання
            def test_func():
                assert ex1.count_min_replacements(array) == result

            return test_func

        globals()[f"test_func_{index}"] = generate_test(arr, res)


counter_tests_generator()

MY_TESTCASE = [
    ([1, 0, 0, 0, 1, 1, 0, 1], 1),
    ([1, 0, 0, 0, 1, 1, 0, 0, 0, 1], 2),
    ([1, 0, 0, 0, 1, 1, 0, 0, 0, 1], 2),
    ([1, 1, 1, 1, 1, 1, 0, 1], 1),
    ([0, 0, 0, 0, 1, 0, 1], 1),
    ([1, 1, 1, 1, 1, 1, 1], 0),
    ([1, 1, 1, 0, 1, 1, 1], 1),
    ([1, 1, 1, 1, 1, 1, 0], 0),
    ([1, 1, 1, 0, 0, 1, 1, 0], 2),
    ([0, 1, 1, 1, 1, 1, 1], 0),
    ([0, 0, 1, 1, 1, 0, 0], 0),
    ([1, 1, 1, 1, 1, 1, 0, 1], 1),
    ([1, 0, 1, 0, 1, 1, 0, 1], 2),
    ([1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0], 3),
    ([1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0], 2),
]
