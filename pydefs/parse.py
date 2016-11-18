# coding=utf-8

import ast
import os


def defs(tree):
    definitions = {}

    indentation_prefix = '↳ '

    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if not isinstance(node.ctx, ast.Load):
                pass
        elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
            name = node.name

            indentation = node.col_offset

            if indentation > 0:
                pad_count = indentation - len(indentation_prefix)
                name = (' ' * pad_count) + indentation_prefix + name

            definitions[node.lineno] = name

    return definitions


def parse_ast(filepath):
    with open(filepath) as file:
        return ast.parse(file.read())


def parse_path(absolute_path):
    if os.path.isfile(absolute_path):
        parse_file(absolute_path)
    else:
        parse_directory(absolute_path)


def parse_file(filepath):
    definitions = defs(parse_ast(filepath))
    definition_count = len(definitions)

    print('{0} ({1} {2})'.format(
        filepath, definition_count, 'definition' if definition_count == 1 else 'definitions'))

    if definition_count > 0:
        last_line_number = max(definitions, key=int)
        zero_pad_length = len(str(last_line_number))

        print_definitions(definitions, zero_pad_length)


def print_definitions(definitions, zero_pad_length):
    for line_number, definition in sorted(definitions.items()):
        print("{0:0{width}d}: {1}".format(line_number, definition, width=zero_pad_length))


def parse_directory(directory_path):
    print(directory_path)

    filenames = [filename for filename in os.listdir(directory_path) if filename.endswith('.py')]

    for filename in filenames:
        filepath = os.path.join(directory_path, filename)

        parse_file(filepath)
