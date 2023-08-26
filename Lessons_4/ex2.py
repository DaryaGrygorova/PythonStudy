test_list = list(range(5)) # [0, 1, 2, 3, 4] - 5 значень

def my_own_range(end):
    counter = 0
    while counter < end:
        yield counter         
        counter += 1 
# оператор yield повертає значення на подобу return 
# але при кожному наступному виклику функції значення 
# що повертається буде залежати від значення що було 
# повернуто раніше у нашому випадку counter += 1 