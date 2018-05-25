def flat(_list):
    """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
    return sum([list(item) for item in _list], [])


def split_snake_case_name_to_words(name):
    return [n for n in name.split('_') if n]
