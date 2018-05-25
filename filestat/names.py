import ast

from .utils.morph_analysis import is_verb


def get_all_names(tree):
    return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]


def get_verbs_from_function_name(function_name):
    return [word for word in function_name.split('_') if is_verb(word)]


def get_all_functions_names(tree):
    return [node.name.lower() for node in ast.walk(tree) if
            isinstance(node, ast.FunctionDef)]
