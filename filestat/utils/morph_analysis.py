from nltk import pos_tag


def is_verb(word):
    if not word:
        return False
    pos_info = pos_tag([word])
    return pos_info[0][1] in ('VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ')


def is_function_name_builtin(name):
    return name.startswith('__') and name.endswith('__')
