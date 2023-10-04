"""
Functions that counts lines and characters in a file
"""

def count_lines(name):
    """Reads an input file and counts the number of lines in it"""
    try:
        with open(name, "r", encoding="UTF-8") as file_obj:
            return len(file_obj.readlines())
    except FileNotFoundError:
        print(f'File "{name}" not found!')
    return None


def count_chars(name):
    """Reads an input file and counts the number of characters in it"""
    try:
        with open(name, "r", encoding="UTF-8") as file_obj:
            return len(file_obj.read())
    except FileNotFoundError:
        print(f'File "{name}" not found!')
    return None


def test(name):
    """Calls functions count_lines(name) and count_chars(name) with a given input file name"""
    lines = count_lines(name)
    chars = count_chars(name)
    return lines, chars


if __name__ == "__main__":
    result = test("mymod.py")
    print(f'File "mymod.py" has {result[0]} lines and {result[1]} chars')

    result2 = test("text_example.txt")
    print(f'File "text_example.txt" has {result2[0]} lines and {result2[1]} chars')
