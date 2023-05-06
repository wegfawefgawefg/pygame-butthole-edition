"""
needs some work, but it's a start"""

import os
import re

source_folder = "./"
prefix = "butthole"


def rename_function_defs(match):
    name = match.group(1)
    return f"def {prefix}_{name}"


def rename_function_calls(match):
    name = match.group(1)
    return f"{prefix}_{name}"


def process_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # Rename function definitions with the format "def function_name", excluding those starting with underscores
    content = re.sub(r"def (?<!_)(\w+)", rename_function_defs, content)

    # First find all function names starting with "def ", excluding those starting with underscores
    function_names = re.findall(r"def (?<!_)(\w+)", content)

    # Rename function calls, excluding those starting with underscores or already having the prefix
    for function_name in function_names:
        content = re.sub(
            rf"(?<![\w_])(?<!{prefix}_){function_name}\(",
            rename_function_calls,
            content,
        )

    with open(file_path, "w") as f:
        f.write(content)


for root, _, files in os.walk(source_folder):
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            process_file(file_path)
