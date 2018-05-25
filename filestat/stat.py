import collections

from .utils.transformation import flat
from .utils.morph_analysis import is_function_name_builtin
from .path import get_trees
from .names import (
    get_all_functions_names,
    get_verbs_from_function_name
)


def get_top_verbs_in_path(path, top_size=10):
    trees = [t for t in get_trees(path) if t]
    function_names = flat(get_all_functions_names(tree) for tree in trees)
    verbs = flat(
        [
            get_verbs_from_function_name(function_name)
            for function_name in function_names if not is_function_name_builtin(function_name)
        ]
    )
    return collections.Counter(verbs).most_common(top_size)


def get_top_functions_names_in_path(path, top_size=10):
    trees = get_trees(path)
    all_functions_names = get_all_functions_names(trees)
    filtered_function_names = [
        f for f in flat(all_functions_names)
        if not (f.startswith('__') and f.endswith('__'))
    ]
    return collections.Counter(filtered_function_names).most_common(top_size)


def show_verbs_occurence(words, top_size=200):
    print('total %s words, %s unique' % (len(words), len(set(words))))
    for word, occurence in collections.Counter(words).most_common(top_size):
        print(word, occurence)
