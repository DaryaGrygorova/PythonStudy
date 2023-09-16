"""
Task 2
Write a decorator that takes a list of stop words
and replaces them with * inside the decorated function
"""


def stop_words(words: list):
    """Takes a list of stop words and replaces them with * inside the decorated function"""
    def wrapper(func):
        def create_new_slogan(name):
            slogan = func(name)

            for word in words:
                slogan = slogan.replace(word, "*")
            return slogan

        return create_new_slogan

    return wrapper


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str) -> str:
    """Create slogan for user with name 'name'"""
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
