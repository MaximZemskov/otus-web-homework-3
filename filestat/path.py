import os
import ast

from .utils.transformation import flat, split_snake_case_name_to_words
from .names import get_all_names


def generate_trees(filenames, with_filenames=False, with_file_content=False):
    if not filenames:
        return []
    trees = []
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as attempt_handler:
            main_file_content = attempt_handler.read()
        try:
            tree = ast.parse(main_file_content)
        except SyntaxError as e:
            print(e)
            tree = None
        if with_filenames:
            if with_file_content:
                trees.append((filename, main_file_content, tree))
            else:
                trees.append((filename, tree))
        else:
            trees.append(tree)
    return trees


def get_trees(path, with_filenames=False, with_file_content=False):
    filenames = get_filenames(path)
    return generate_trees(filenames, with_filenames, with_file_content)


def get_filenames(path):
    filenames = []
    for dirname, dirs, files in os.walk(path, topdown=True):
        for file in files:
            if file.endswith('.py'):
                filenames.append(os.path.join(dirname, file))
    return filenames


def get_all_words_in_path(path):
    trees = [t for t in get_trees(path) if t]
    all_names = [get_all_names(t) for t in trees]
    function_names = [f for f in flat(all_names)
                      if not (f.startswith('__') and f.endswith('__'))]
    return flat(
        [split_snake_case_name_to_words(function_name)
         for function_name in function_names]
    )


